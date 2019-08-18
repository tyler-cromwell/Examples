import React, { Fragment, useState, useEffect } from 'react'

function HookCounter() {
  const [count, setCount] = useState(0)
  const [name, setName] = useState('')
  const [x, setX] = useState(0)
  const [y, setY] = useState(0)

  const logMousePosition = (e) => {
    setX(e.clientX)
    setY(e.clientY)
  }

  // Equivalent to componentDidUpdate (unconditional)
  useEffect(() => {
    console.log('[Hook] useEffect')
  })

  // Equivalent to componentDidUpdate (conditional)
  useEffect(() => {
    document.title = `Hook 02: clicked ${count} times`
    console.log('[Hook] Updated document title')
  }, [count])

  // Equivalent to componentDidMount and componentWillUnmount
  useEffect(() => {
    window.addEventListener('mousemove', logMousePosition)
    console.log('[Hook] Added event listener to: mousemove')
    return () => {
      window.removeEventListener('mousemove', logMousePosition)
      console.log('[Hook] Removed event listener from: mousemove')
      console.log('[Hook] Component unmounted')
    }
  }, [])

  return (
    <Fragment>
      Hook Count: {count}
      <button onClick={() => setCount(count+1)}>Increment</button>
      <input type="text" value={name} onChange={(e) => setName(e.target.value)}/>
      <div>
        (x = {x}, y = {y})
      </div>
    </Fragment>
  )
}

export default HookCounter
