import React, { useState, useEffect } from 'react';
import { format } from 'date-fns';

interface DiaryEntry {
  id?: number;
  entry_date: string;
  title?: string;
  body?: string;
  mood?: string;
  favorite?: boolean;
}

interface EntryEditorProps {
  entry?: DiaryEntry;
  onSave: (entry: DiaryEntry) => void;
  onCancel: () => void;
}

const EntryEditor: React.FC<EntryEditorProps> = ({ entry, onSave, onCancel }) => {
  const [formData, setFormData] = useState<DiaryEntry>({
    entry_date: entry?.entry_date || format(new Date(), 'yyyy-MM-dd'),
    title: entry?.title || '',
    body: entry?.body || '',
    mood: entry?.mood || '',
    favorite: entry?.favorite || false
  });
  
  const [isSaving, setIsSaving] = useState(false);
  
  useEffect(() => {
    // If entry changes, update form data
    if (entry) {
      setFormData({
        entry_date: entry.entry_date,
        title: entry.title || '',
        body: entry.body || '',
        mood: entry.mood || '',
        favorite: entry.favorite || false
      });
    }
  }, [entry]);
  
  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement>) => {
    const { name, value, type } = e.target as HTMLInputElement | HTMLTextAreaElement | HTMLSelectElement;
    const checked = (e.target as HTMLInputElement).checked;
    
    setFormData(prev => ({
      ...prev,
      [name]: type === 'checkbox' ? checked : value
    }));
  };
  
  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setIsSaving(true);
    
    try {
      await onSave(formData);
    } finally {
      setIsSaving(false);
    }
  };
  
  return (
    <form onSubmit={handleSubmit} className="entry-editor">
      <div className="editor-header">
        <input
          type="text"
          name="title"
          placeholder="Entry title"
          value={formData.title}
          onChange={handleChange}
          className="entry-title"
        />
        <div className="editor-meta">
          <span className="entry-date">{format(new Date(formData.entry_date), 'MMMM d, yyyy')}</span>
        </div>
      </div>
      
      <div className="editor-body">
        <textarea
          name="body"
          placeholder="Write your diary entry here..."
          value={formData.body}
          onChange={handleChange}
          className="entry-body"
        />
      </div>
      
      <div className="editor-controls">
        <div className="mood-selector">
          <label>Mood:</label>
          <select
            name="mood"
            value={formData.mood}
            onChange={handleChange}
          >
            <option value="">Select mood</option>
            <option value="Happy">Happy</option>
            <option value="Sad">Sad</option>
            <option value="Excited">Excited</option>
            <option value="Anxious">Anxious</option>
            <option value="Content">Content</option>
            <option value="Tired">Tired</option>
          </select>
        </div>
        
        <div className="favorite-toggle">
          <label>
            <input
              type="checkbox"
              name="favorite"
              checked={formData.favorite}
              onChange={handleChange}
            />
            Favorite
          </label>
        </div>
        
        <div className="editor-actions">
          <button 
            type="button" 
            onClick={onCancel} 
            className="btn btn-secondary"
          >
            Cancel
          </button>
          <button 
            type="submit" 
            disabled={isSaving}
            className="btn btn-primary"
          >
            {isSaving ? 'Saving...' : 'Save Entry'}
          </button>
        </div>
      </div>
    </form>
  );
};

export default EntryEditor;