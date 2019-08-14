import React, { useState, useEffect } from 'react'

function HookCounter() {
  const [count, setCount] = useState(0)
  const [name, setName] = useState('')
  const [x, setX] = useState(0)
  const [y, setY] = useState(0)

  const logMousePosition = (e) => {
    setX(e.clientX)
    setY(e.clientY)
  }

  useEffect(() => {
    console.log('[Hook] useEffect')
  })

  useEffect(() => {
    document.title = `Hook 02: clicked ${count} times`
    console.log('[Hook] Updated document title')
  }, [count])

  useEffect(() => {
    window.addEventListener('mousemove', logMousePosition)
    console.log('[Hook] Added event listener to: mousemove')
  }, [])

  return (
    <div>
      Hook Count: {count}
      <button onClick={() => setCount(count+1)}>Increment</button>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)}/>
      <div>
        (x = {x}, y = {y})
      </div>
    </div>
  )
}

export default HookCounter
