import React from 'react';
import Main from './components/Main/Main';

// Define the types for the component's props
interface MyComponentProps {
  
}

const App: React.FC<MyComponentProps> = () => {
  return (
    <div>
      <Main/>
    </div>
  );
};

export default App;