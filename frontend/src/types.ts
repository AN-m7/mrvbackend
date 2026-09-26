export interface User {
  id: number;
  email: string;
  name: string;
  is_admin: boolean;
  created_at: string;
}

export interface Product {
  id: number;
  name: string;
  category: string;
  price: number;
  stock: number;
  is_active: boolean;
  created_at: string;
}

export interface DashboardStats {
  total_users: number;
  total_products: number;
  active_products: number;
  low_stock_products: number;
  total_revenue: number;
  sales_trend: Array<{ name: string; value: number }>;
  category_breakdown: Array<{ name: string; value: number }>;
}
