const API_BASE = "http://127.0.0.1:8000/api";

export async function checkHealth() {
    try {
        const res = await fetch(`${API_BASE}/health/`);
        const data = await res.json();
        return (data.status === "ok");
    } catch (err) {
        console.error("Health check failed:", err);
    }
}

export async function getAuthStatus() {
    try {
        const res = await fetch(`${API_BASE}/auth_status/`, {
            credentials: "include",
        });
        return await res.json();
    } catch (err) {
        console.error("Auth status failed:", err);
        return { authenticated: false };
    }
}

async function getCsrfToken() {
    const cookies = await chrome.cookies.getAll({ url: API_BASE.replace("/api", "") });
    const csrfCookie = cookies.find(c => c.name === "csrftoken");
    return csrfCookie ? csrfCookie.value : null;
}

export async function postSiteEvent(url, tabId, eventType, timestamp) {
    console.log("Trying to post site event: ", url, tabId, eventType, timestamp)
    try {
        const csrfToken = await getCsrfToken();
        const headers = {
            "Content-Type": "application/json",
        };
        if (csrfToken) {
            headers["X-CSRFToken"] = csrfToken;
        }
        const res = await fetch(`${API_BASE}/events/`, {
            method: "POST",
            credentials: "include",
            headers,
            body: JSON.stringify({
                events: [{
                    url,
                    tab_id: tabId,
                    event_type: eventType,
                    timestamp,
                }],
            }),
        });
        if (!res.ok) {
            const error = await res.json();
            throw new Error(`HTTP ${res.status}: ${JSON.stringify(error)}`);
        }
        return await res.json();
    } catch (err) {
        console.error("Failed to post site event:", err);
        return null;
    }
}

export async function addSubscription(name, url) {
    try {
        const csrfToken = await getCsrfToken();
        const headers = { "Content-Type": "application/json" };
        if (csrfToken) headers["X-CSRFToken"] = csrfToken;
        const res = await fetch(`${API_BASE}/subscriptions/add/`, {
            method: "POST",
            credentials: "include",
            headers,
            body: JSON.stringify({ name, url }),
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (err) {
        console.error("Failed to add subscription:", err);
        return null;
    }
}

export async function deleteSubscription(id) {
    try {
        const csrfToken = await getCsrfToken();
        const headers = {};
        if (csrfToken) headers["X-CSRFToken"] = csrfToken;
        const res = await fetch(`${API_BASE}/subscriptions/${id}/`, {
            method: "DELETE",
            credentials: "include",
            headers,
        });
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        return await res.json();
    } catch (err) {
        console.error("Failed to delete subscription:", err);
        return null;
    }
}

export async function getSubscriptions() {
    try {
        const res = await fetch(`${API_BASE}/subscriptions/`, {
            credentials: "include",
        });
        if (!res.ok) {
            throw new Error(`HTTP ${res.status}`);
        }
        const data = await res.json();
        return data.subscriptions || [];
    } catch (err) {
        console.error("Failed to fetch subscriptions:", err);
        return [];
    }
}
