import { fetchRules } from "@/lib/api";
import ChecklistClient from "../components/ChecklistClient";
export default async function ChecklistPage() {
  const rules = await fetchRules();

  return <ChecklistClient rules={rules} />;
}