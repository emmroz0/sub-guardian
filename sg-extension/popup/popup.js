import { checkHealth, getAuthStatus } from "../js/api.js";

document.addEventListener("DOMContentLoaded", async () => {
    const statusEl = document.getElementById("api-status");
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
    }
});
