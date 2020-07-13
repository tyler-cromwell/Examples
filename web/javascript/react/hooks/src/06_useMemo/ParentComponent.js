import React, { useMemo, useState } from 'react'


function ParentComponent() {
  const [value1, setValue1] = useState(0)
  const [value2, setValue2] = useState(0)

  const increment1 = () => {
    setValue1(value1 + 1)
  }

  const increment2 = () => {
    setValue2(value2 + 1)
  }

  const isEven = useMemo(() => {
    for (let i = 0; i < 1000000000; i++);
    return value1 % 2 === 0
  }, [value1])

  return (
    <div>
      <div>
        <button onClick={increment1}>{value1}</button>
        <span>{isEven ? 'Even' : 'Odd'}</span>
      </div>
      <div>
        <button onClick={increment2}>{value2}</button>
      </div>
    </div>
  )
}


export default ParentComponent
