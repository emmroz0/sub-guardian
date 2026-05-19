import { checkHealth, getAuthStatus, getSubscriptions, addSubscription, deleteSubscription } from "../js/api.js";
import { getSiteName } from "../js/helpers.js";

let matchedSub = null;
let tabUrl = null;
let siteName = null;

async function refreshTabStatus(tabStatusEl, btn) {
    const subs = await getSubscriptions();
    siteName = getSiteName(tabUrl);
    matchedSub = subs.find(s => s.name === siteName);
    if (matchedSub) {
        tabStatusEl.textContent = `Active tab is in subscription: ${matchedSub.name}`;
        tabStatusEl.classList.remove("text-warning");
        tabStatusEl.classList.add("text-success");
        btn.textContent = "Remove from subscriptions";
        btn.style.display = "";
    } else {
        tabStatusEl.textContent = "Active tab is not in any subscription";
        tabStatusEl.classList.remove("text-success");
        tabStatusEl.classList.add("text-warning");
        btn.textContent = "Add to subscriptions";
        btn.style.display = "";
    }
}

document.addEventListener("DOMContentLoaded", async () => {
    const statusEl = document.getElementById("api-status");
    const tabStatusEl = document.getElementById("tab-status");
    const toggleBtn = document.getElementById("toggle-sub-btn");
    const ok = await checkHealth();
    if (!ok) {
        statusEl.textContent = "Offline";
        statusEl.classList.add("text-danger");
        return;
    }
    const auth = await getAuthStatus();
    if (auth.authenticated) {
        statusEl.textContent = `Logged as ${auth.username}`;
        statusEl.classList.add("text-success");
    } else {
        statusEl.textContent = "Not logged in";
        statusEl.classList.add("text-warning");
        toggleBtn.style.display = "none";
        return;
    }

    const [tab] = await chrome.tabs.query({ active: true, currentWindow: true });
    if (!tab?.url) return;
    tabUrl = tab.url;
    await refreshTabStatus(tabStatusEl, toggleBtn);

    toggleBtn.addEventListener("click", async () => {
        toggleBtn.disabled = true;
        if (matchedSub) {
            await deleteSubscription(matchedSub.id);
        } else {
            await addSubscription(siteName, tabUrl);
        }
        await refreshTabStatus(tabStatusEl, toggleBtn);
        toggleBtn.disabled = false;
    });
});
