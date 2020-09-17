<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p v-if="errors.length">
      <b>Please correct the following error(s):</b>
      <ul>
        <li v-for="error in errors">{{ error }}</li>
      </ul>
    </p>
    <form @submit="checkForm" method="get" action="/">
      <table>
        <tr>
          <td><label>X-Coordinate:</label></td>
          <td><input v-model="xcoordinate" placeholder="y-coordinate"></td>
        </tr>
        <tr>
          <td><label>Y-Coordinate:</label></td>
          <td><input v-model="ycoordinate" placeholder="y-coordinate"></td>
        </tr>
        <tr>
          <td><label>N of points:</label></td>
          <td><input v-model.number="points" placeholder="points"></td>
        </tr>
        <tr>
          <td><label>Option:</label></td>
          <td>
            <select v-model="selected">
              <option disabled value="">Please select one</option>
              <option>Nearest</option>
              <option>furthest</option>
            </select>
          </td>
        </tr>
        <tr>
          <td>
            <input type="submit" value="Submit">
          </td>
        </tr>
      </table>
    </form>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      msg: 'Simple form with the desired data',
      errors: [],
      points: 0,
      xcoordinate: 0.0,
      ycoordinate: 0.0,
      selected: ''
    }
  },
  methods: {
    checkForm: function (e) {
      if (this.xcoordinate && this.ycoordinate && this.points > 0 && this.selected) {
        return true
      }

      this.errors = []
      console.log()
      if (!this.xcoordinate || isNan(parseFloat(this.xcoordinate))) {
        this.errors.push('X Coordinate is required and must be a float number')
        console.error(this.xcoordinate)
      }
      if (!this.ycoordinate || isNan(parseFloat(this.xcoordinate))) {
        this.errors.push('Y Coordinate is required')
      }
      if (!this.points || isNan(parseInt(this.points)) ) {
        this.errors.push('Points is required')
      }
      if (!this.selected) {
        this.errors.push('Selection is required')
      }
      e.preventDefault()
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
