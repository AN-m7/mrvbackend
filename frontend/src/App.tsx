:root {
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
  line-height: 1.5;
  font-weight: 400;
  color: #e2e8f0;
  background: #020817;
  font-synthesis: none;
  text-rendering: optimizeLegibility;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
}

* {
  box-sizing: border-box;
}

html, body, #root {
  margin: 0;
  min-height: 100%;
  height: 100%;
  background: #020817;
}

body {
  min-height: 100vh;
}

a {
  color: inherit;
  text-decoration: none;
}

button,
input {
  font: inherit;
}

.auth-shell {
  min-height: 100vh;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, #020817, #0f172a 50%, #111827);
  padding: 24px;
}

.auth-card {
  width: min(420px, 100%);
  background: rgba(15, 23, 42, 0.9);
  border: 1px solid rgba(148, 163, 184, 0.2);
  border-radius: 22px;
  padding: 32px;
  box-shadow: 0 32px 80px rgba(2, 8, 23, 0.75);
}

.auth-header h1 {
  margin: 10px 0 8px;
  font-size: 2rem;
}

.auth-header p {
  margin: 0 0 20px;
  color: #94a3b8;
}

.badge {
  display: inline-block;
  padding: 6px 12px;
  border-radius: 999px;
  background: rgba(59, 130, 246, 0.14);
  color: #7dd3fc;
  font-size: 0.75rem;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.auth-form {
  display: grid;
  gap: 16px;
}

.auth-form label {
  display: grid;
  gap: 8px;
  color: #cbd5e1;
  font-size: 0.92rem;
}

.auth-form input {
  width: 100%;
  border: 1px solid #334155;
  border-radius: 12px;
  background: #0f172a;
  color: white;
  padding: 12px 14px;
}

.auth-form button,
.logout-btn,
.inline-form button,
.product-item button {
  border: none;
  border-radius: 12px;
  cursor: pointer;
  transition: opacity 0.2s ease;
}

.auth-form button {
  background: linear-gradient(135deg, #2563eb, #38bdf8);
  color: white;
  padding: 12px 16px;
  font-weight: 700;
}

.error-box {
  background: rgba(239, 68, 68, 0.12);
  border: 1px solid rgba(239, 68, 68, 0.3);
  color: #fca5a5;
  border-radius: 10px;
  padding: 10px 12px;
}

.app-layout {
  display: grid;
  grid-template-columns: 240px minmax(0, 1fr);
  min-height: 100vh;
}

.sidebar {
  background: #0f172a;
  border-right: 1px solid #1e293b;
  padding: 24px 18px;
}

.brand {
  font-size: 1.6rem;
  font-weight: 800;
  margin-bottom: 24px;
  letter-spacing: 0.06em;
}

.sidebar nav {
  display: grid;
  gap: 12px;
}

.sidebar nav a,
.logout-btn {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  padding: 10px 12px;
  border-radius: 12px;
  background: #111827;
  color: #e2e8f0;
  border: 1px solid #1f2937;
}

.logout-btn {
  background: #7f1d1d;
  border: none;
  margin-top: 8px;
}

.main-panel {
  padding: 28px;
}

.page-panel {
  background: rgba(15, 23, 42, 0.7);
  border: 1px solid rgba(148, 163, 184, 0.14);
  border-radius: 20px;
  padding: 24px;
}

.page-header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.subtitle {
  margin: 0;
  font-size: 0.8rem;
  color: #7dd3fc;
  letter-spacing: 0.08em;
  text-transform: uppercase;
}

.page-header h2 {
  margin: 6px 0 0;
  font-size: 2rem;
}

.stats-grid,
.admin-summary {
  display: grid;
  gap: 16px;
  grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
  margin-bottom: 24px;
}

.stat-card,
.summary-card {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 16px;
  padding: 18px 16px;
  display: grid;
  gap: 10px;
}

.stat-card span,
.summary-card span {
  color: #94a3b8;
}

.stat-card strong,
.summary-card strong {
  font-size: 1.8rem;
}

.stat-card.accent {
  background: linear-gradient(135deg, rgba(37, 99, 235, 0.25), rgba(56, 189, 248, 0.08));
}

.charts-grid,
.admin-columns {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
  gap: 20px;
}

.chart-card,
.panel-box {
  background: #0f172a;
  border: 1px solid #1e293b;
  border-radius: 16px;
  padding: 18px;
}

.chart-card h3,
.panel-box h3 {
  margin-top: 0;
}

.inline-form {
  display: grid;
  gap: 12px;
  margin-bottom: 18px;
}

.inline-form input {
  background: #020817;
  border: 1px solid #334155;
  border-radius: 12px;
  padding: 10px 12px;
  color: white;
}

.checkbox-row {
  display: flex;
  align-items: center;
  gap: 8px;
  color: #cbd5e1;
}

.inline-form button,
.product-item button {
  background: #2563eb;
  color: white;
  padding: 10px 12px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th, td {
  text-align: left;
  padding: 10px 8px;
  border-bottom: 1px solid #1e293b;
}

.product-list {
  display: grid;
  gap: 12px;
}

.product-item {
  display: flex;
  justify-content: space-between;
  gap: 12px;
  align-items: center;
  background: #020817;
  border: 1px solid #1e293b;
  border-radius: 12px;
  padding: 12px;
}

.product-item p {
  margin: 6px 0 0;
  color: #94a3b8;
}

.loading-screen {
  min-height: 100vh;
  display: grid;
  place-items: center;
  color: #cbd5e1;
  font-size: 1.1rem;
}

@media (max-width: 860px) {
  .app-layout {
    grid-template-columns: 1fr;
  }

  .sidebar {
    border-right: none;
    border-bottom: 1px solid #1e293b;
  }

  .main-panel {
    padding: 18px;
  }
}
