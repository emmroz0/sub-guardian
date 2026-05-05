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
