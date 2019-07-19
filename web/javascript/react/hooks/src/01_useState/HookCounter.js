import React, {useState} from 'react'

function HookCounter() {
  const initialCount = 0
  const [count, setCount] = useState(initialCount)
  const [name, setName] = useState({firstName: '', lastName: ''})
  const [items, setItems] = useState([])

  const increment5f = () => {
    for (let i = 0; i < 5; i++) {
      // Does not update the state: setCount(count+1)
      setCount(count => count + 1)
    }
  }

  const addItem = () => {
    setItems([...items, {
      id: items.length,
      value: Math.floor(Math.random() * 10) + 1
    }])
  }

  return (
    <div>
      Hook Count: {count}
      <button onClick={() => setCount(initialCount)}>Reset</button>
      <button onClick={() => setCount(count+1)}>Increment</button>
      <button onClick={() => setCount(count-1)}>Decrement</button>
      <button onClick={() => setCount(count+5)}>Increment 5</button>
      <button onClick={increment5f}>Increment 5 (f)</button>

      <form>
        <input
          type='text'
          value={name.firstName}
          onChange={e => setName({...name, firstName: e.target.value})}
        />
        <input
          type='text'
          value={name.lastName}
          onChange={e => setName({...name, lastName: e.target.value})}
        />
        <p>
          Your first name is: {name.firstName}<br/>
          Your last name is: {name.lastName}
        </p>
      </form>

      <button onClick={addItem}>Hooks: Add number</button>
      <ul>
        {items.map(item => (
          <li key={item.id}>{item.value}</li>
        ))}
      </ul>
    </div>
  )
}

export default HookCounter
