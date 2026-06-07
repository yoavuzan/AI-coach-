import React from 'react';
import CoachChat from '../components/CoachChat';
import VoiceButton from '../components/VoiceButton';

const Chat: React.FC = () => {
  return (
    <div className="flex flex-col items-center w-full min-h-[calc(100vh-80px)] py-8">
      <h1 className="text-3xl font-bold mb-2">AI Coach</h1>
      <p className="text-gray-400 mb-8">Get personalized advice and stay motivated.</p>
      
      <div className="w-full max-w-[800px] flex-1 flex flex-col items-center">
        <CoachChat />
        
        <div className="mt-12 flex flex-col items-center gap-4">
          <p className="text-sm text-gray-500 font-medium">Or use voice commands</p>
          <VoiceButton />
        </div>
      </div>
    </div>
  );
};

export default Chat;
