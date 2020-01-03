import React from 'react';
import logo from './logo.svg';
import './App.css';

import { default as ClassCounter01 } from './01_useState/ClassCounter'
import { default as HookCounter01 } from './01_useState/HookCounter'

import { default as Container02 } from './02_useEffect/Container02'

import { default as RegularComponent03 } from './03_useContext/RegularComponent03'
import { default as HookComponent03 } from './03_useContext/HookComponent03'

import { default as StateCounter } from './04_useReducer/StateCounter'
import { default as ReducerCounter } from './04_useReducer/ReducerCounter'

import { default as ParentComponent } from './05_useCallback/ParentComponent'

export const UserContext = React.createContext()
export const ChannelContext = React.createContext()


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
          <Container02/>
        </div>

        <div className="Separation">
          <h2>Hook 3: useContext</h2>
          <UserContext.Provider value={'tyler'}>
            <ChannelContext.Provider value={'Examples'}>
              <RegularComponent03/>
              <HookComponent03/>
            </ChannelContext.Provider>
          </UserContext.Provider>
        </div>

        <div className="Separation">
          <h2>Hook 4: useReducer</h2>
          <StateCounter/>
          <ReducerCounter/>
        </div>

        <div className="Seperation">
          <h2>Hook 5: useCallback</h2>
          <ParentComponent/>
        </div>
      </div>
    </div>
  );
}

export default App;
