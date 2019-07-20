import React, { useState, useEffect } from 'react'

function HookCounter() {
  const [count, setCount] = useState(0)

  useEffect(() => {
    document.title = `Hook 02: clicked ${count} times`
  })

  return (
    <div>
      Hook Count: {count}
      <button onClick={() => setCount(count+1)}>Increment</button>
    </div>
  )
}

export default HookCounter
