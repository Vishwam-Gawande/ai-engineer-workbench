import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import MainLayout from "../layouts/MainLayout";

import DashboardPage from "../pages/Dashboard/DashboardPage";
import TracesPage from "../pages/Traces/TracesPage";
import PromptsPage from "../pages/Prompts/PromptsPage";
import ExperimentsPage from "../pages/Experiments/ExperimentsPage";
import SettingsPage from "../pages/Settings/SettingsPage";

export default function AppRoutes() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route
          path="/dashboard"
          element={
            <MainLayout>
              <DashboardPage />
            </MainLayout>
          }
        />

        <Route
          path="/traces"
          element={
            <MainLayout>
              <TracesPage />
            </MainLayout>
          }
        />

        <Route
          path="/prompts"
          element={
            <MainLayout>
              <PromptsPage />
            </MainLayout>
          }
        />

        <Route
          path="/experiments"
          element={
            <MainLayout>
              <ExperimentsPage />
            </MainLayout>
          }
        />

        <Route
          path="/settings"
          element={
            <MainLayout>
              <SettingsPage />
            </MainLayout>
          }
        />
      </Routes>
    </BrowserRouter>
  );
}