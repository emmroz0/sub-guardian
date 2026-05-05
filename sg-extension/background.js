import { getSubscriptions } from "./js/api.js";
import { getSiteName } from "./js/helpers.js";

let subscriptionsCache = [];

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
//refreshSubscriptions();

chrome.tabs.onCreated.addListener(async (tab) => {
    await refreshSubscriptions();
    const isSubscription = matchesSubscription(tab.url, subscriptionsCache);
    console.log("Tab created:", {
        tabId: tab.id,
        url: tab.url || "(empty)",
        createdAt: new Date().toISOString(),
        isSubscription,
    });
});

chrome.tabs.onRemoved.addListener((tabId, removeInfo) => {
    console.log("Tab removed:", {
        tabId: tabId,
        removedAt: new Date().toISOString(),
        windowId: removeInfo.windowId,
    });
});

chrome.tabs.onUpdated.addListener(async (tabId, changeInfo, tab) => {
    if (changeInfo.status !== "complete") {
        return;
    }
    await refreshSubscriptions();
    const siteName = getSiteName(tab.url)
    const isSubscription = matchesSubscription(siteName, subscriptionsCache);
    console.log("Tab updated (loaded):", {
        tabId: tab.id,
        url: tab.url || "(empty)",
        updatedAt: new Date().toISOString(),
        site: siteName,
        isSubscription: isSubscription,
    });
});
