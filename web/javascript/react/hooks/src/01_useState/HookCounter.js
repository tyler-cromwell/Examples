import React, {useState} from 'react'

function HookCounter() {
  const initialCount = 0
  const [count, setCount] = useState(initialCount)

  const increment5f = () => {
    for (let i = 0; i < 5; i++) {
      //setCount(count+1)
      setCount(count => count + 1)
    }
  }

  return (
    <div>
      Hook Count: {count}
      <button onClick={() => setCount(initialCount)}>Reset</button>
      <button onClick={() => setCount(count+1)}>Increment</button>
      <button onClick={() => setCount(count-1)}>Decrement</button>
      <button onClick={() => setCount(count+5)}>Increment 5</button>
      <button onClick={increment5f}>Increment 5 (f)</button>
    </div>
  )
}

export default HookCounter
