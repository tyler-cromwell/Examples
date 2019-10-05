import React, { Component, Fragment } from 'react'

class ClassCounter extends Component {
  constructor(props) {
    super(props)
    this.state = {
      count: 0,
      name: '',
      x: 0,
      y: 0
    }
  }

  logMousePosition = (e) => {
    this.setState({
      x: e.clientX,
      y: e.clientY,
    })
  }

  incrementCount = () => {
    this.setState({
      count: this.state.count + 1
    })
  }

  updateName = (e) => {
    this.setState({
      name: e.target.value
    })
  }

  // Equiavlent to useEffect with []
  componentDidMount() {
    document.title = `Class 02: clicked ${this.state.count} times`
    window.addEventListener('mousemove', this.logMousePosition)
    console.log('[Class] Added event listener to: mousemove')
  }

  // Equivalent to useEffect / useEffect [count]
  componentDidUpdate(prevProps, prevState) {
    console.log('[Class] componentDidUpdate')
    if (prevState.count !== this.state.count) {
      document.title = `Class 02: clicked ${this.state.count} times`
      console.log('[Class] Updated document title')
    }
  }

  // Equivalent to useEffect cleanup function
  componentWillUnmount() {
    window.removeEventListener('mousemove', this.logMousePosition)
    console.log('[Class] Removed event listener from: mousemove')
    console.log('[Class] Component unmounted')
  }

  render() {
    return (
      <Fragment>
        Class Count: {this.state.count}
        <button onClick={this.incrementCount}>Increment</button>
        <input type="text" value={this.state.name} onChange={this.updateName} placeholder="Open the developer console"/>
        <div>
          (x = {this.state.x}, y = {this.state.y})
        </div>
      </Fragment>
    )
  }
}

export default ClassCounter
