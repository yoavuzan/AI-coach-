import React from 'react';
import { Mic } from 'lucide-react';

const VoiceButton: React.FC = () => {
  const [isListening, setIsListening] = React.useState(false);

  const toggleListening = () => {
    setIsListening(!isListening);
    // Voice implementation placeholder
  };

  return (
    <button 
      className={`w-[60px] h-[60px] rounded-full flex items-center justify-center cursor-pointer transition-all duration-200 border-none outline-none shadow-[0_4px_12px_rgba(100,108,255,0.4)] ${
        isListening 
          ? 'bg-[#ff4d4d] animate-pulse-slow' 
          : 'bg-[#646cff] hover:scale-110 hover:bg-[#535bf2]'
      }`}
      onClick={toggleListening}
      title="Voice Command"
    >
      <Mic size={24} color="#fff" />
    </button>
  );
};

export default VoiceButton;
