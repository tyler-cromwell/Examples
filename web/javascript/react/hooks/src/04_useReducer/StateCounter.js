import React, { useState } from 'react'


function StateCounter() {
  const [count, setCount] = useState(0)

  return (
    <div>
      <div>State Count: {count}</div>
      <button onClick={() => setCount(count+1)}>+1</button>
      <button onClick={() => setCount(count-1)}>-1</button>
      <button onClick={() => setCount(0)}>Reset</button>
    </div>
  )
}


export default StateCounter
