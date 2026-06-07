import { create } from 'zustand';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'ai';
  timestamp: Date;
}

interface AIState {
  messages: Message[];
  isThinking: boolean;
  addMessage: (message: Omit<Message, 'id' | 'timestamp'>) => void;
  setThinking: (thinking: boolean) => void;
  clearChat: () => void;
}

export const useAIStore = create<AIState>((set) => ({
  messages: [
    { 
      id: '1', 
      text: "Hello! I'm your AI Habit Coach. How can I help you today?", 
      sender: 'ai',
      timestamp: new Date()
    },
  ],
  isThinking: false,
  addMessage: (msg) => set((state) => ({ 
    messages: [...state.messages, { ...msg, id: Date.now().toString(), timestamp: new Date() }] 
  })),
  setThinking: (thinking) => set({ isThinking: thinking }),
  clearChat: () => set({ messages: [] }),
}));
