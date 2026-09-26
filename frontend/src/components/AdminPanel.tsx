import {
  BarChart,
  Bar,
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  XAxis,
  YAxis,
  Tooltip,
  CartesianGrid,
} from "recharts";

import { DashboardStats } from "../types";

const COLORS = ["#3b82f6", "#22c55e", "#f59e0b", "#ef4444", "#8b5cf6", "#14b8a6"];

interface DashboardPageProps {
  stats: DashboardStats;
}

export default function DashboardPage({ stats }: DashboardPageProps) {
  return (
    <div className="page-panel">
      <div className="page-header">
        <div>
          <p className="subtitle">Overview</p>
          <h2>Dashboard</h2>
        </div>
      </div>

      <div className="stats-grid">
        <div className="stat-card">
          <span>Total users</span>
          <strong>{stats.total_users}</strong>
        </div>
        <div className="stat-card">
          <span>Total products</span>
          <strong>{stats.total_products}</strong>
        </div>
        <div className="stat-card">
          <span>Active products</span>
          <strong>{stats.active_products}</strong>
        </div>
        <div className="stat-card accent">
          <span>Revenue estimate</span>
          <strong>${stats.total_revenue.toFixed(2)}</strong>
        </div>
      </div>

      <div className="charts-grid">
        <div className="chart-card">
          <h3>Inventory by category</h3>
          <ResponsiveContainer width="100%" height={260}>
            <BarChart data={stats.sales_trend}>
              <CartesianGrid strokeDasharray="3 3" stroke="#334155" />
              <XAxis dataKey="name" stroke="#cbd5e1" />
              <YAxis stroke="#cbd5e1" />
              <Tooltip />
              <Bar dataKey="value" fill="#60a5fa" radius={[8, 8, 0, 0]} />
            </BarChart>
          </ResponsiveContainer>
        </div>

        <div className="chart-card">
          <h3>Category mix</h3>
          <ResponsiveContainer width="100%" height={260}>
            <PieChart>
              <Pie data={stats.category_breakdown} dataKey="value" nameKey="name" outerRadius={80} label>
                {stats.category_breakdown.map((entry, index) => (
                  <Cell key={`${entry.name}-${index}`} fill={COLORS[index % COLORS.length]} />
                ))}
              </Pie>
              <Tooltip />
            </PieChart>
          </ResponsiveContainer>
        </div>
      </div>
    </div>
  );
}
