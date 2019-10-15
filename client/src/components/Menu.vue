<template>
  <div class="container">
    <div class="row">
      <div class="col-sm-10">
        <br>
        <h1>Menue</h1>
        <alert :message="message" v-if="showMessage"></alert>
        <hr><br><br>
        <button type="button" class="btn btn-success btn-sm" v-b-modal.user-modal>Add Item</button>
        <br><br>
        <table class="table table-hover">
          <thead>
            <tr>
              <th scope="col">Name</th>
              <th scope="col">Email</th>
              <th>Actions</th>
            </tr>
          </thead>
          <tbody>
            <tr v-for="(user, index) in users" :key="index">
              <td>{{ user.first_name }} {{ user.last_name }}</td>
              <td>{{ user.email }}</td>
             
              <td>
                <div class="btn-group" role="group">
                  <button
				        type="button"
				        class="btn btn-info btn-sm"
				        v-b-modal.user-update-modal
				        @click="editUser(user)">
				    Update
				</button>
                  <button
				        type="button"
				        class="btn btn-danger btn-sm"
				        @click="onDeleteUser(user)">
				    Delete
				</button>
                </div>
              </td>
            </tr>
          </tbody>
        </table>
      </div>

  	<b-modal ref="addUserModal"
         id="user-modal"
         title="Add a new user"
         hide-footer>
		  <b-form @submit="onSubmit" @reset="onReset" class="w-100">
		  <b-form-group id="form-title-group"
		                label="First Name:"
		                label-for="form-title-input">
		      <b-form-input id="form-title-input"
		                    type="text"
		                    v-model="addUserForm.first_name"
		                    required
		                    placeholder="Enter First Name">
		      </b-form-input>
		    </b-form-group>
		    <b-form-group id="form-author-group"
		                  label="Last Name:"
		                  label-for="form-author-input">
		        <b-form-input id="form-author-input"
		                      type="text"
		                      v-model="addUserForm.last_name"
		                      required
		                      placeholder="Enter Last Name">
		        </b-form-input>
	      	</b-form-group>
	      	<b-form-group id="form-author-group"
		                  label="Email:"
		                  label-for="form-author-input">
		        <b-form-input id="form-author-input"
		                      type="text"
		                      v-model="addUserForm.email"
		                      required
		                      placeholder="Enter Email">
		        </b-form-input>
	      	</b-form-group>
		   
		    <b-button type="submit" variant="primary">Submit</b-button>
		    <b-button type="reset" variant="danger">Reset</b-button>
		  </b-form>
	</b-modal>

	<b-modal ref="editUserModal"
         id="user-update-modal"
         title="Update"
         hide-footer>
  <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
  <b-form-group id="form-title-edit-group"
                label="First Name:"
                label-for="form-title-edit-input">
      <b-form-input id="form-title-edit-input"
                    type="text"
                    v-model="editUserForm.first_name"
                    required
                    placeholder="Enter First Name">
      </b-form-input>
    </b-form-group>
    <b-form-group id="form-author-edit-group"
                  label="Last Name:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="editUserForm.last_name"
                      required
                      placeholder="Enter author">
        </b-form-input>
      </b-form-group>
      <b-form-group id="form-author-edit-group"
                  label="Email:"
                  label-for="form-author-edit-input">
        <b-form-input id="form-author-edit-input"
                      type="text"
                      v-model="editUserForm.email"
                      required
                      placeholder="Enter Email">
        </b-form-input>
      </b-form-group>
    
    <b-button-group>
      <b-button type="submit" variant="primary">Update</b-button>
      <b-button type="reset" variant="danger">Cancel</b-button>
    </b-button-group>
  </b-form>
</b-modal>

    </div>
  </div>
</template>

<script>
import axios from 'axios';
import Alert from './Alert.vue';

export default {
  data() {
    return {
      users: [],
      addUserForm: {
        first_name: '',
        last_name: '',
        email: '',
      },
      editUserForm: {
      	id: '',
        first_name: '',
        last_name: '',
        email: '',
      },
      message:'',
      showMessage: false,
    };
  },
  components: {
    alert: Alert,
  },
  methods: {
    getUsers() {
      const path = 'http://localhost:5000/api/users';
      axios.get(path)
        .then((res) => {
          this.users = res.data.data;
          //console.log(res.data.data)
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.error(error);
        });
    },
    addUser(payload) {
      const path = 'http://localhost:5000/api/users';
      axios.post(path, payload)
        .then(() => {
          this.getUsers();
          this.message = 'User added!';
          this.showMessage = true;
        })
        .catch((error) => {
          // eslint-disable-next-line
          console.log(error);
          this.getUsers();
        });
    },
    editUser(user) {
	  this.editUserForm = user;
	},
    initForm() {
      this.addUserForm.first_name = '';
      this.addUserForm.first_name = '';
      this.addUserForm.email = '';
      this.editUserForm.id = '';
      this.editUserForm.first_name = '';
      this.editUserForm.first_name = '';
      this.editUserForm.email = '';
    },
    onSubmit(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      
      const payload = {
        first_name: this.addUserForm.first_name,
        last_name: this.addUserForm.last_name,
        email: this.addUserForm.email,
      };
      this.addUser(payload);
      this.initForm();
    },
    onSubmitUpdate(evt) {
	  evt.preventDefault();
	  this.$refs.editUserModal.hide();
	  const payload = {
	    first_name: this.editUserForm.first_name,
	    last_name: this.editUserForm.last_name,
	    email: this.editUserForm.email,
	  };
	  this.updateUser(payload, this.editUserForm.id);
	},
	updateUser(payload, userId) {
	  const path = `http://localhost:5000/api/users/${userId}`;
	  axios.put(path, payload)
	    .then(() => {
	      this.getUsers();
	      this.message = 'User updated!';
	      this.showMessage = true;
	    })
	    .catch((error) => {
	      // eslint-disable-next-line
	      console.error(error);
	      this.getUsers();
	    });
	},
	onResetUpdate(evt) {
	  evt.preventDefault();
	  this.$refs.editUserModal.hide();
	  this.initForm();
	  this.getUsers(); // why?
	},
    onReset(evt) {
      evt.preventDefault();
      this.$refs.addUserModal.hide();
      this.initForm();
    },
    removeUser(userId) {
	  const path = `http://localhost:5000/api/users/${userId}`;
	  axios.delete(path)
	    .then(() => {
	      this.getUsers();
	      this.message = 'User removed!';
	      this.showMessage = true;
	    })
	    .catch((error) => {
	      // eslint-disable-next-line
	      console.error(error);
	      this.getUsers();
	    });
	},
	onDeleteUser(user) {
	  this.removeUser(user.id);
	},
  },
  created() {
    this.getUsers();
  },
};
</script>