import { getSubscriptions, postSiteEvent } from "./js/api.js";
import { getSiteName } from "./js/helpers.js";

let subscriptionsCache = [];
const tabUrls = new Map();

async function refreshSubscriptions() {
    try {
        subscriptionsCache = await getSubscriptions();
    } catch (err) {
        console.error("Failed to refresh subscriptions:", err);
    }
    return subscriptionsCache;
}

function matchesSubscription(siteName, subscriptions) {
    return subscriptions.some(element => {
        return siteName === element.name;
    });
}

chrome.tabs.onCreated.addListener(async (tab) => {
    if (!tab.url || tab.url.startsWith("chrome://") || tab.url.startsWith("chrome-extension://")) {
        return;
    }
    tabUrls.set(tab.id, tab.url);
    await refreshSubscriptions();
    const siteName = getSiteName(tab.url);
    const isSubscription = matchesSubscription(siteName, subscriptionsCache);
    if (isSubscription) {
        await postSiteEvent(tab.url, tab.id, "open", new Date().toISOString());
    }
    console.log("Tab created:", {
        tabId: tab.id,
        url: tab.url || "(empty)",
        createdAt: new Date().toISOString(),
        site: siteName,
        isSubscription,
    });
});

chrome.tabs.onRemoved.addListener(async (tabId, removeInfo) => {
    const url = tabUrls.get(tabId);
    if (url) {
        await refreshSubscriptions();
        const siteName = getSiteName(url);
        const isSubscription = matchesSubscription(siteName, subscriptionsCache);
        if (isSubscription) {
            await postSiteEvent(url, tabId, "close", new Date().toISOString());
        }
        tabUrls.delete(tabId);
        console.log("Tab removed:", {
            tabId: tabId,
            url,
            site: siteName,
            removedAt: new Date().toISOString(),
            windowId: removeInfo.windowId,
            isSubscription,
        });
    } else {
        console.log("Tab removed (no tracked URL):", { tabId });
    }
});

chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
    if (changeInfo.status !== "complete") {
        return;
    }
    if (!tab.url || tab.url.startsWith("chrome://") || tab.url.startsWith("chrome-extension://")) {
        return;
    }
    tabUrls.set(tabId, tab.url);
    await refreshSubscriptions();
    const siteName = getSiteName(tab.url)
    const isSubscription = matchesSubscription(siteName, subscriptionsCache);
    if (isSubscription) {
        await postSiteEvent(tab.url, tabId, "open", new Date().toISOString());
    }
    console.log("Tab updated (loaded):", {
        tabId: tab.id,
        url: tab.url || "(empty)",
        updatedAt: new Date().toISOString(),
        site: siteName,
        isSubscription: isSubscription,
    });
});
