import { create } from 'zustand';

interface Habit {
  id: string;
  name: string;
  description: string;
  frequency: string;
  streak: number;
}

interface HabitState {
  habits: Habit[];
  addHabit: (habit: Habit) => void;
  removeHabit: (id: string) => void;
}

export const useHabitStore = create<HabitState>((set) => ({
  habits: [
    { id: '1', name: 'Drink Water', description: 'Drink 8 glasses of water', frequency: 'Daily', streak: 5 },
    { id: '2', name: 'Exercise', description: '30 mins of physical activity', frequency: 'Daily', streak: 3 },
  ],
  addHabit: (habit) => set((state) => ({ habits: [...state.habits, habit] })),
  removeHabit: (id) => set((state) => ({ habits: state.habits.filter((h) => h.id !== id) })),
}));
