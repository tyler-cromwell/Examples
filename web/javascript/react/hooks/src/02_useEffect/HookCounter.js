import React, { useState, useEffect } from 'react'

function HookCounter() {
  const [count, setCount] = useState(0)
  const [name, setName] = useState('')

  useEffect(() => {
    console.log('[Hook] useEffect')
  })

  useEffect(() => {
    console.log('[Hook] Updating document title...')
    document.title = `Hook 02: clicked ${count} times`
  }, [count])

  return (
    <div>
      Hook Count: {count}
      <button onClick={() => setCount(count+1)}>Increment</button>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)}/>
    </div>
  )
}

export default HookCounter
