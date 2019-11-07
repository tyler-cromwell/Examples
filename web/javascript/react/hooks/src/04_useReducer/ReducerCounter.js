import React, { useReducer } from 'react'


const initialState = 0
const reducer = (state, action) => {
  switch(action.type) {
    case 'increment':
      return state + action.value
    case 'decrement':
      return state - action.value
    case 'reset':
      return 0
    default:
      return state
  }
}


function ReducerCounter() {
  const [count, dispatch] = useReducer(reducer, initialState)

  return (
    <div>
      <div>ReducerCount: {count}</div>
      <button onClick={() => dispatch({type: 'increment', value: 2})}>+2</button>
      <button onClick={() => dispatch({type: 'decrement', value: 2})}>-2</button>
      <button onClick={() => dispatch({type: 'reset'})}>Reset</button>
    </div>
  )
}


export default ReducerCounter
