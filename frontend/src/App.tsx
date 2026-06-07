import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './pages/Dashboard';
import Login from './pages/Login';
import Progress from './pages/Progress';
import Settings from './pages/Settings';
import AddHabit from './pages/AddHabit';

function App() {
  return (
    <Router>
      <Navbar />
      <div className="max-w-[1200px] mx-auto px-8 pb-8 w-full">
        <Routes>
          <Route path="/" element={<Dashboard />} />
          <Route path="/login" element={<Login />} />
          <Route path="/progress" element={<Progress />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/add-habit" element={<AddHabit />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App;
