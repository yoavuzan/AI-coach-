import React, { useState } from 'react';
import { Send } from 'lucide-react';

interface Message {
  id: string;
  text: string;
  sender: 'user' | 'ai';
}

const CoachChat: React.FC = () => {
  const [messages, setMessages] = useState<Message[]>([
    { id: '1', text: "Hello! I'm your AI Habit Coach. How can I help you today?", sender: 'ai' },
  ]);
  const [input, setInput] = useState('');

  const handleSend = () => {
    if (!input.trim()) return;
    
    const userMsg: Message = { id: Date.now().toString(), text: input, sender: 'user' };
    setMessages([...messages, userMsg]);
    setInput('');
    
    // Simulate AI response
    setTimeout(() => {
      const aiMsg: Message = { 
        id: (Date.now() + 1).toString(), 
        text: "That sounds like a great goal! I'll help you stay on track.", 
        sender: 'ai' 
      };
      setMessages((prev) => [...prev, aiMsg]);
    }, 1000);
  };

  return (
    <div className="flex flex-col h-[400px] w-full max-w-[600px] bg-[#2a2a2a] rounded-xl overflow-hidden mt-12 shadow-lg">
      <div className="flex-1 p-4 overflow-y-auto flex flex-col gap-3">
        {messages.map((msg) => (
          <div 
            key={msg.id} 
            className={`p-3.5 px-4 rounded-xl max-w-[80%] text-sm ${
              msg.sender === 'ai' 
                ? 'bg-[#3a3a3a] text-white self-start rounded-bl-none' 
                : 'bg-[#646cff] text-white self-end rounded-br-none'
            }`}
          >
            {msg.text}
          </div>
        ))}
      </div>
      <div className="flex p-4 bg-[#1a1a1a] gap-2">
        <input 
          type="text" 
          value={input} 
          onChange={(e) => setInput(e.target.value)}
          placeholder="Type a message..."
          className="flex-1 bg-[#3a3a3a] border-none rounded-lg px-4 py-2.5 text-white outline-none focus:ring-1 focus:ring-[#646cff]"
          onKeyPress={(e) => e.key === 'Enter' && handleSend()}
        />
        <button 
          onClick={handleSend}
          className="bg-[#646cff] hover:bg-[#535bf2] text-white border-none rounded-lg w-10 h-10 flex items-center justify-center cursor-pointer transition-colors"
        >
          <Send size={20} />
        </button>
      </div>
    </div>
  );
};

export default CoachChat;
