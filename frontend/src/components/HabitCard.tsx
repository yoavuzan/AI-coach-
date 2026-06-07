import React from 'react';
import { Check, Flame } from 'lucide-react';

interface HabitCardProps {
  name: string;
  description: string;
  streak: number;
}

const HabitCard: React.FC<HabitCardProps> = ({ name, description, streak }) => {
  return (
    <div className="bg-[#2a2a2a] rounded-xl p-6 flex flex-col justify-between text-left shadow-lg transition-transform hover:-translate-y-1">
      <div className="mb-4">
        <h3 className="text-lg font-semibold text-white mb-2">{name}</h3>
        <p className="text-gray-400 text-sm leading-relaxed">{description}</p>
      </div>
      <div className="mt-4 flex justify-between items-center">
        <span className="flex items-center gap-1.5 text-[#ff9f43] font-bold text-sm">
          <Flame size={16} /> {streak} day streak
        </span>
        <button className="bg-[#28c76f] hover:bg-[#20a15b] text-white rounded-full w-10 h-10 flex items-center justify-center transition-colors cursor-pointer border-none outline-none">
          <Check size={20} />
        </button>
      </div>
    </div>
  );
};

export default HabitCard;
