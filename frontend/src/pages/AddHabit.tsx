import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useHabitStore } from '../store/habitStore';

const AddHabit: React.FC = () => {
  const [name, setName] = useState('');
  const [description, setDescription] = useState('');
  const [frequency, setFrequency] = useState('Daily');
  const addHabit = useHabitStore((state) => state.addHabit);
  const navigate = useNavigate();

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    if (!name.trim()) return;

    addHabit({
      id: Date.now().toString(),
      name,
      description,
      frequency,
      streak: 0,
    });
    navigate('/');
  };

  return (
    <div className="flex flex-col items-center w-full">
      <h1 className="text-3xl font-bold mb-8">Add New Habit</h1>
      <form onSubmit={handleSubmit} className="bg-[#2a2a2a] p-8 rounded-xl w-full max-w-[500px] flex flex-col gap-6 text-left shadow-lg">
        <div className="flex flex-col gap-2">
          <label className="font-bold text-white">Habit Name</label>
          <input 
            type="text" 
            value={name} 
            onChange={(e) => setName(e.target.value)} 
            placeholder="e.g., Read for 30 mins" 
            required 
            className="bg-[#3a3a3a] border border-[#444] rounded-lg p-3 text-white outline-none focus:ring-1 focus:ring-[#646cff]"
          />
        </div>
        <div className="flex flex-col gap-2">
          <label className="font-bold text-white">Description</label>
          <textarea 
            value={description} 
            onChange={(e) => setDescription(e.target.value)} 
            placeholder="What is your goal?" 
            className="bg-[#3a3a3a] border border-[#444] rounded-lg p-3 text-white outline-none focus:ring-1 focus:ring-[#646cff] min-h-[100px]"
          />
        </div>
        <div className="flex flex-col gap-2">
          <label className="font-bold text-white">Frequency</label>
          <select 
            value={frequency} 
            onChange={(e) => setFrequency(e.target.value)}
            className="bg-[#3a3a3a] border border-[#444] rounded-lg p-3 text-white outline-none focus:ring-1 focus:ring-[#646cff]"
          >
            <option value="Daily">Daily</option>
            <option value="Weekly">Weekly</option>
            <option value="Monthly">Monthly</option>
          </select>
        </div>
        <button type="submit" className="bg-[#646cff] hover:bg-[#535bf2] text-white border-none rounded-lg p-4 font-bold cursor-pointer transition-colors mt-4">
          Create Habit
        </button>
      </form>
    </div>
  );
};

export default AddHabit;
