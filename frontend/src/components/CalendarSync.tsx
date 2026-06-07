import React from 'react';
import { Calendar, RefreshCw } from 'lucide-react';

const CalendarSync: React.FC = () => {
  return (
    <div className="bg-[#2a2a2a] p-6 rounded-xl text-left shadow-lg">
      <div className="flex items-center gap-3 mb-4 text-[#646cff]">
        <Calendar size={20} />
        <h4 className="m-0 text-white font-semibold">Calendar Sync</h4>
      </div>
      <p className="text-sm text-gray-400 mb-6">Sync your habits with Google Calendar to get reminders.</p>
      <button className="bg-[#3a3a3a] hover:bg-[#4a4a4a] text-white border border-[#444] px-4 py-2.5 rounded-lg cursor-pointer flex items-center gap-2 text-sm transition-colors outline-none">
        <RefreshCw size={16} /> Sync Now
      </button>
    </div>
  );
};

export default CalendarSync;
