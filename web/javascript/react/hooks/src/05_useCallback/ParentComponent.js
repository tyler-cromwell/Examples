import React, { useCallback, useState } from 'react'

import { default as Count } from './CountComponent'
import { default as Button } from './ButtonComponent'


function ParentComponent() {
  const [value1, setValue1] = useState(0)
  const [value2, setValue2] = useState(0)

  const increment1 = useCallback(() => {
    setValue1(value1 + 1)
  }, [value1])

  const increment2 = useCallback(() => {
    setValue2(value2 + 1)
  }, [value2])

  return (
    <div>
      <Count text="Value 1" count={value1}/>
      <Button handler={increment1}>Increment 1</Button>
      <Count text="Value 2" count={value2}/>
      <Button handler={increment2}>Increment 2</Button>
    </div>
  )
}


export default ParentComponent
