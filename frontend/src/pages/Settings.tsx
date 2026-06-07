import React from 'react';
import { User, Bell, Shield, Globe } from 'lucide-react';
import { useUserStore } from '../store/userStore';

const Settings: React.FC = () => {
  const { user, updatePreferences } = useUserStore();

  if (!user) return null;

  return (
    <div className="flex flex-col items-center w-full">
      <h1 className="text-3xl font-bold mb-8">Settings</h1>
      
      <div className="w-full max-w-[600px] flex flex-col gap-8 text-left mt-8">
        <section className="bg-[#2a2a2a] p-6 rounded-xl shadow-lg">
          <h3 className="flex items-center gap-2 m-0 border-b border-[#444] pb-2 text-white font-semibold mb-4">
            <User size={20} className="text-[#646cff]" /> Profile
          </h3>
          <div className="flex justify-between items-center mt-4">
            <span className="text-gray-400">Username</span>
            <span className="text-[#646cff] font-medium">{user.name}</span>
          </div>
          <div className="flex justify-between items-center mt-4">
            <span className="text-gray-400">Email</span>
            <span className="text-[#646cff] font-medium">{user.email}</span>
          </div>
        </section>

        <section className="bg-[#2a2a2a] p-6 rounded-xl shadow-lg">
          <h3 className="flex items-center gap-2 m-0 border-b border-[#444] pb-2 text-white font-semibold mb-4">
            <Bell size={20} className="text-[#646cff]" /> Notifications
          </h3>
          <div className="flex justify-between items-center mt-4">
            <span className="text-gray-400">Daily Reminders</span>
            <input 
              type="checkbox" 
              checked={user.preferences.notifications} 
              onChange={(e) => updatePreferences({ notifications: e.target.checked })}
              className="w-5 h-5 accent-[#646cff] cursor-pointer"
            />
          </div>
        </section>

        <section className="bg-[#2a2a2a] p-6 rounded-xl shadow-lg">
          <h3 className="flex items-center gap-2 m-0 border-b border-[#444] pb-2 text-white font-semibold mb-4">
            <Globe size={20} className="text-[#646cff]" /> Preferences
          </h3>
          <div className="flex justify-between items-center mt-4">
            <span className="text-gray-400">Language</span>
            <select 
              value={user.preferences.language} 
              onChange={(e) => updatePreferences({ language: e.target.value })}
              className="bg-[#3a3a3a] border border-[#444] rounded-lg p-2 text-white outline-none focus:ring-1 focus:ring-[#646cff]"
            >
              <option value="English">English</option>
              <option value="Hebrew">Hebrew</option>
              <option value="Spanish">Spanish</option>
            </select>
          </div>
          <div className="flex justify-between items-center mt-4">
            <span className="text-gray-400">Theme</span>
            <select 
              value={user.preferences.theme} 
              onChange={(e) => updatePreferences({ theme: e.target.value as 'light' | 'dark' })}
              className="bg-[#3a3a3a] border border-[#444] rounded-lg p-2 text-white outline-none focus:ring-1 focus:ring-[#646cff]"
            >
              <option value="dark">Dark</option>
              <option value="light">Light</option>
            </select>
          </div>
        </section>

        <section className="bg-[#2a2a2a] p-6 rounded-xl shadow-lg">
          <h3 className="flex items-center gap-2 m-0 border-b border-[#444] pb-2 text-white font-semibold mb-4">
            <Shield size={20} className="text-[#646cff]" /> Security
          </h3>
          <button className="bg-[#3a3a3a] hover:bg-[#4a4a4a] text-white border border-[#444] px-4 py-2 rounded-lg cursor-pointer transition-colors mt-4 text-sm">
            Change Password
          </button>
        </section>
      </div>
    </div>
  );
};

export default Settings;
