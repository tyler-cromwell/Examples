import React, { Fragment, useState } from 'react'

import { default as ClassCounter02 } from './ClassCounter'
import { default as HookCounter02 } from './HookCounter'

function Container02() {
  const [enabledClass, setEnabledClass] = useState(true)
  const [enabledHook, setEnabledHook] = useState(true)

  return (
    <Fragment>
      <div>
        <button onClick={() => setEnabledClass(!enabledClass)}>Class Toggle</button>
        {enabledClass && <ClassCounter02/>}
      </div>
      <div>
        <button onClick={() => setEnabledHook(!enabledHook)}>Hook Toggle</button>
        {enabledHook && <HookCounter02/>}
      </div>
    </Fragment>
  )
}

export default Container02
