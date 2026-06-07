import { create } from 'zustand';

interface User {
  id: string;
  name: string;
  email: string;
  avatar?: string;
  preferences: {
    theme: 'light' | 'dark';
    notifications: boolean;
    language: string;
  };
}

interface UserState {
  user: User | null;
  isAuthenticated: boolean;
  setUser: (user: User) => void;
  updatePreferences: (prefs: Partial<User['preferences']>) => void;
  logout: () => void;
}

export const useUserStore = create<UserState>((set) => ({
  user: {
    id: '1',
    name: 'Demo User',
    email: 'demo@example.com',
    preferences: {
      theme: 'dark',
      notifications: true,
      language: 'English',
    },
  },
  isAuthenticated: true,
  setUser: (user) => set({ user, isAuthenticated: true }),
  updatePreferences: (prefs) => set((state) => ({
    user: state.user ? {
      ...state.user,
      preferences: { ...state.user.preferences, ...prefs }
    } : null
  })),
  logout: () => set({ user: null, isAuthenticated: false }),
}));
