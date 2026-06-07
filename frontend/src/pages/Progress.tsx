import React from 'react';
import { useHabitStore } from '../store/habitStore';
import { BarChart, TrendingUp, Calendar } from 'lucide-react';

const Progress: React.FC = () => {
  const habits = useHabitStore((state) => state.habits);
  const totalStreaks = habits.reduce((acc, habit) => acc + habit.streak, 0);

  return (
    <div className="flex flex-col items-center w-full">
      <h1 className="text-3xl font-bold mb-8">Your Progress</h1>
      
      <div className="grid grid-cols-[repeat(auto-fit,minmax(200px,1fr))] gap-6 w-full">
        <div className="bg-[#2a2a2a] p-6 rounded-xl flex items-center gap-4 shadow-lg border border-transparent hover:border-[#646cff] transition-colors">
          <TrendingUp className="text-[#646cff]" size={32} />
          <div className="flex flex-col">
            <span className="text-xs text-gray-400 uppercase tracking-wider font-semibold">Total Streaks</span>
            <span className="text-2xl font-bold text-white">{totalStreaks}</span>
          </div>
        </div>
        <div className="bg-[#2a2a2a] p-6 rounded-xl flex items-center gap-4 shadow-lg border border-transparent hover:border-[#646cff] transition-colors">
          <BarChart className="text-[#646cff]" size={32} />
          <div className="flex flex-col">
            <span className="text-xs text-gray-400 uppercase tracking-wider font-semibold">Active Habits</span>
            <span className="text-2xl font-bold text-white">{habits.length}</span>
          </div>
        </div>
        <div className="bg-[#2a2a2a] p-6 rounded-xl flex items-center gap-4 shadow-lg border border-transparent hover:border-[#646cff] transition-colors">
          <Calendar className="text-[#646cff]" size={32} />
          <div className="flex flex-col">
            <span className="text-xs text-gray-400 uppercase tracking-wider font-semibold">Completion Rate</span>
            <span className="text-2xl font-bold text-white">85%</span>
          </div>
        </div>
      </div>

      <div className="mt-12 w-full text-left">
        <h2 className="text-xl font-bold mb-6">Habit Breakdown</h2>
        <div className="flex flex-col gap-6">
          {habits.map((habit) => (
            <div key={habit.id} className="w-full">
              <div className="flex justify-between items-center mb-2">
                <span className="font-semibold text-white">{habit.name}</span>
                <span className="text-sm text-gray-400">{habit.streak} days</span>
              </div>
              <div className="bg-[#3a3a3a] h-2.5 rounded-full overflow-hidden">
                <div 
                  className="bg-[#646cff] h-full transition-all duration-500 ease-out shadow-[0_0_10px_rgba(100,108,255,0.5)]" 
                  style={{ width: `${Math.min((habit.streak / 30) * 100, 100)}%` }}
                ></div>
              </div>
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default Progress;
