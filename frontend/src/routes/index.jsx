import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";

import DashboardPage from "../pages/Dashboard/DashboardPage";
import TracesPage from "../pages/Traces/TracesPage";
import PromptsPage from "../pages/Prompts/PromptsPage";
import ExperimentsPage from "../pages/Experiments/ExperimentsPage";
import SettingsPage from "../pages/Settings/SettingsPage";

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Navigate to="/dashboard" replace />} />

        <Route path="/dashboard" element={<DashboardPage />} />
        <Route path="/traces" element={<TracesPage />} />
        <Route path="/prompts" element={<PromptsPage />} />
        <Route path="/experiments" element={<ExperimentsPage />} />
        <Route path="/settings" element={<SettingsPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;