import React from 'react';
import HabitCard from '../components/HabitCard';
import CalendarSync from '../components/CalendarSync';
import WeeklyReport from '../components/WeeklyReport';
import { useHabitStore } from '../store/habitStore';

const Dashboard: React.FC = () => {
  const habits = useHabitStore((state) => state.habits);

  return (
    <div className="flex flex-col items-center w-full">
      <h1 className="text-3xl font-bold mb-2">Dashboard</h1>
      <p className="text-gray-400">Welcome to your AI Habit Coach!</p>
      
      <div className="grid grid-cols-[repeat(auto-fill,minmax(300px,1fr))] gap-6 w-full mt-8">
        {habits.map((habit) => (
          <HabitCard
            key={habit.id}
            name={habit.name}
            description={habit.description}
            streak={habit.streak}
          />
        ))}
      </div>

      <div className="grid grid-cols-[repeat(auto-fit,minmax(300px,1fr))] gap-6 w-full mt-12">
        <CalendarSync />
        <WeeklyReport />
      </div>
    </div>
  );
};

export default Dashboard;
