import Sidebar from "../components/common/Sidebar";
import Topbar from "../components/common/Topbar";

export default function MainLayout({ children }) {
  return (
    <div
      style={{
        display: "flex",
        minHeight: "100vh",
        background: "#f5f7fb",
      }}
    >
      <Sidebar />

      <div style={{ flex: 1 }}>
        <Topbar />

        <main
          style={{
            padding: "32px",
          }}
        >
          {children}
        </main>
      </div>
    </div>
  );
}