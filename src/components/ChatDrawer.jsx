import React, { useState, useEffect, useRef } from 'react';
import { MessageSquare, Send, X } from 'lucide-react';

export default function ChatDrawer({
  isOpen,
  activeRide,
  messages,
  onClose,
  onOpenDefault,
  onSendMessage
}) {
  const [inputText, setInputText] = useState('');
  const messagesEndRef = useRef(null);

  // Auto-scroll to bottom whenever messages update or drawer opens
  useEffect(() => {
    if (isOpen && messagesEndRef.current) {
      messagesEndRef.current.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages, isOpen]);

  const handleSend = (e) => {
    e.preventDefault();
    if (!inputText.trim()) return;
    onSendMessage(inputText.trim());
    setInputText('');
  };

  const getInitials = (name) => {
    if (!name) return '🛺';
    return name
      .split(' ')
      .map(n => n[0])
      .join('')
      .toUpperCase();
  };

  return (
    <>
      {/* Floating Chat Trigger Button */}
      {!isOpen && (
        <div 
          className="chat-trigger" 
          id="chat-trigger-btn"
          onClick={onOpenDefault}
          title="Open Coordination Chat"
        >
          <MessageSquare size={24} />
        </div>
      )}

      {/* Slide-over Chat Panel */}
      <div className={`chat-panel ${isOpen ? 'active' : ''}`} id="chat-drawer">
        <div className="chat-header">
          <div className="chat-user-info">
            <div className="chat-user-avatar" id="chat-group-avatar">
              {activeRide ? getInitials(activeRide.creatorName) : '🛺'}
            </div>
            <div>
              <h4 style={{ fontSize: '0.95rem', fontWeight: 700 }} id="chat-group-title">
                {activeRide ? `${activeRide.creatorName}'s Ride` : 'Autoshare Coordination'}
              </h4>
              <span style={{ fontSize: '0.75rem', color: 'var(--color-success)', display: 'flex', alignItems: 'center', gap: '4px' }}>
                ● Online
              </span>
            </div>
          </div>
          <button 
            className="modal-close" 
            id="close-chat-btn"
            onClick={onClose}
            aria-label="Close Chat"
            style={{ width: '28px', height: '28px' }}
          >
            <X size={16} />
          </button>
        </div>

        <div className="chat-messages" id="chat-box">
          {(!messages || messages.length === 0) ? (
            <div style={{ textAlign: 'center', color: 'var(--text-muted)', fontSize: '0.85rem', padding: '3rem 1rem' }}>
              No coordination messages yet. Start the conversation!
            </div>
          ) : (
            messages.map((msg, index) => {
              const isSystem = msg.sender === 'System';
              const isMe = msg.sender === 'You';

              if (isSystem) {
                return (
                  <div 
                    key={index} 
                    style={{
                      textAlign: 'center',
                      color: 'var(--text-muted)',
                      fontSize: '0.75rem',
                      margin: '0.4rem 0',
                      fontStyle: 'italic'
                    }}
                  >
                    {msg.text}
                  </div>
                );
              }

              return (
                <div 
                  key={index} 
                  className={`message ${isMe ? 'sent' : 'received'}`}
                >
                  <div style={{ fontSize: '0.7rem', fontWeight: 'bold', marginBottom: '2px' }}>
                    {msg.sender}
                  </div>
                  <div>{msg.text}</div>
                  <div className="message-time">{msg.time}</div>
                </div>
              );
            })
          )}
          <div ref={messagesEndRef} />
        </div>

        <form className="chat-input-area" onSubmit={handleSend}>
          <input 
            type="text" 
            id="chat-input-field"
            placeholder="Type coordination message..."
            value={inputText}
            onChange={(e) => setInputText(e.target.value)}
          />
          <button 
            type="submit" 
            className="chat-send-btn" 
            id="send-chat-message-btn"
            aria-label="Send Message"
          >
            <Send size={18} />
          </button>
        </form>
      </div>
    </>
  );
}
