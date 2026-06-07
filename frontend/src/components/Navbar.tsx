import React from 'react';
import { Link } from 'react-router-dom';

const Navbar: React.FC = () => {
  return (
    <nav className="flex justify-between items-center px-8 py-4 bg-[#1a1a1a] text-white w-full fixed top-0 left-0 box-border z-[1000] shadow-md">
      <div className="font-bold text-lg text-[#646cff]">Habit Coach</div>
      <div className="flex gap-6">
        <Link to="/" className="text-white hover:text-[#646cff] no-underline text-sm transition-colors">Dashboard</Link>
        <Link to="/chat" className="text-white hover:text-[#646cff] no-underline text-sm transition-colors">AI Coach</Link>
        <Link to="/progress" className="text-white hover:text-[#646cff] no-underline text-sm transition-colors">Progress</Link>
        <Link to="/add-habit" className="text-white hover:text-[#646cff] no-underline text-sm transition-colors">Add Habit</Link>
        <Link to="/login" className="text-white hover:text-[#646cff] no-underline text-sm transition-colors">Login</Link>
      </div>
    </nav>
  );
};

export default Navbar;
