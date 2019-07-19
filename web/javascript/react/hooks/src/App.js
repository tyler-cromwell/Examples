import React from 'react';
import logo from './logo.svg';
import './App.css';

import { default as ClassCounter01 } from './01_useState/ClassCounter'
import { default as HookCounter01 } from './01_useState/HookCounter'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>
      </header>

      <div className="Content">
        <div className="Separation">
          <h2>Hook 1: useState</h2>
          <ClassCounter01/>
          <HookCounter01/>
        </div>

        <div className="Separation">
          <h2>Hook 2: useEffect</h2>
        </div>
      </div>
    </div>
  );
}

export default App;
