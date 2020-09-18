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
          <td><input id="xcoordinate" v-model="xcoordinate" placeholder="y-coordinate"></td>
          <td><label>Load from history</label></td>
          <td>
            <select v-model="history" v-on:change="fillInputBox">
              <option disabled value="">Please select one</option>
              <option v-for="option in options" v-bind:value="option.text">
                {{option.text}}
              </option>
            </select>
          </td>
        </tr>
        <tr>
          <td><label>Y-Coordinate:</label></td>
          <td><input id="ycoordinate" v-model="ycoordinate" placeholder="y-coordinate"></td>
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
            <input type="submit" value="Get Coordinates">
          </td>
        </tr>
      </table>
    </form>
  </div>
</template>

<script>
export default {
  name: 'GetCoordinate',
  data () {
    return {
      msg: 'Simple form with the desired data',
      errors: [],
      history: 'Choose',
      options: [],
      points: 0,
      xcoordinate: 0.0,
      ycoordinate: 0.0,
      selected: ''
    }
  },
  mounted () {
    this.getRequestHistory(this)
  },
  methods: {
    checkForm: function (e) {
      if (this.xcoordinate && this.ycoordinate && this.points > 0 && this.selected) {
        return true
      }

      this.errors = []
      if (!this.xcoordinate || isNaN(parseFloat(this.xcoordinate))) {
        this.errors.push('X Coordinate is required and must be a float number')
      }
      if (!this.ycoordinate || isNaN(parseFloat(this.xcoordinate))) {
        this.errors.push('Y Coordinate is required')
      }
      if (!this.points || isNaN(parseInt(this.points))) {
        this.errors.push('Points is required')
      }
      if (!this.selected) {
        this.errors.push('Selection is required')
      }
      e.preventDefault()
    },
    getRequestHistory (vm) {
      fetch('http://127.0.0.1:8000/api/v1/history/', {
        method: 'GET',
        credentials: 'same-origin'
      })
        .then((response) => response.json())
        .then(function(data) {
          var historyList = []
          var i
          for (i = 0; i < data.length; i++) {
            historyList.push({text: data[i]['x_axes'] + '|' + data[i]['y_axes']  + '|' + data[i]['points']})
          }
          vm.options = historyList
        })
    },
    fillInputBox () {
      this.xcoordinate = this.history.split('|')[0]
      this.ycoordinate = this.history.split('|')[1]
      this.points = this.history.split('|')[2]
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
