        // Profile Modal handling
        const profileModal = document.getElementById('profileModal');
        const profileClose = profileModal.querySelector('.close');
        const profileTableBody = document.getElementById('profile-table-body');

        // User Update Modal handling
        const userUpdateModal = document.getElementById('userUpdateModal');
        const userUpdateClose = userUpdateModal.querySelector('.close');

        // Function to fetch and populate profile table
        async function fetchAndPopulateProfiles() {
            const accessToken = localStorage.getItem('access_token');
            if (!accessToken) {
                alert("No access token found. Please log in.");
                return false;
            }

            try {
                const response = await fetch('/api/v1/users/get_all_user_data', {
                    method: 'GET',
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Content-Type': 'application/json',
                    },
                });
                const data = await response.json();
                if (data.error) {
                    alert("Error fetching profiles: " + data.error);
                    return false;
                }
                if (!response.ok) {
                    alert("Error fetching profiles: " + data.message);
                    return false;
                }

                // Check if users array exists
                if (!data.users || !Array.isArray(data.users)) {
                    alert("No user profile data available.");
                    return false;
                }

                // Clear existing table rows
                profileTableBody.innerHTML = '';

                // If no users, show a placeholder row
                if (data.users.length === 0) {
                    profileTableBody.innerHTML = '<tr><td colspan="9">No users available.</td></tr>';
                } else {
                    // Populate table with all users
                    data.users.forEach(user => {
                        const row = document.createElement('tr');
                        row.innerHTML = `
                            <td>${user.first_name || 'N/A'}</td>
                            <td>${user.last_name || 'N/A'}</td>
                            <td>${user.email || 'N/A'}</td>
                            <td>${user.password ? '********' : 'N/A'}</td>
                            <td>${user.role || 'N/A'}</td>
                            <td>${user.department || 'N/A'}</td>
                            <td>${user.phone_number || 'N/A'}</td>
                            <td>${user.status || 'N/A'}</td>
                            <td>
                                <button class="update-user" data-id="${user.email}">Update</button>
                                <button class="delete-user" data-id="${user.email}">Delete</button>
                            </td>
                        `;
                        profileTableBody.appendChild(row);
                    });
                }
                return true;
            } catch (error) {
                alert("Error fetching profiles: " + error.message);
                return false;
            }
        }

        // Open Profile Modal
        document.querySelector('.get-profile').addEventListener('click', async function() {
            const success = await fetchAndPopulateProfiles();
            if (success) {
                profileModal.style.display = 'block';
                document.body.style.overflow = 'hidden';
            }
        });

        // Update User
        document.addEventListener('click', async function(event) {
            if (event.target.classList.contains('update-user')) {
                const email = event.target.getAttribute('data-id');
                const row = event.target.closest('tr');
                const cells = row.getElementsByTagName('td');

                // Populate update modal
                document.getElementById('update_user_email').value = email;
                document.getElementById('update_first_name').value = cells[0].textContent !== 'N/A' ? cells[0].textContent : '';
                document.getElementById('update_last_name').value = cells[1].textContent !== 'N/A' ? cells[1].textContent : '';
                document.getElementById('update_email_display').value = email;
                document.getElementById('update_role').value = cells[4].textContent !== 'N/A' ? cells[4].textContent : '';
                document.getElementById('update_department').value = cells[5].textContent !== 'N/A' ? cells[5].textContent : '';
                document.getElementById('update_phone_number').value = cells[6].textContent !== 'N/A' ? cells[6].textContent : '';
                document.getElementById('update_user_status').value = cells[7].textContent !== 'N/A' ? cells[7].textContent : '';

                userUpdateModal.style.display = 'block';
                document.body.style.overflow = 'hidden';
            }
        });

        // Delete User
        document.addEventListener('click', async function(event) {
            if (event.target.classList.contains('delete-user')) {
                const email = event.target.getAttribute('data-id');
                if (!confirm(`Are you sure you want to delete user ${email}?`)) {
                    return;
                }

                const accessToken = localStorage.getItem('access_token');
                if (!accessToken) {
                    alert("No access token found. Please log in.");
                    return;
                }

                try {
                    const response = await fetch(`/api/v1/admin/delete_user/${email}`, {
                        method: 'DELETE',
                        headers: {
                            'Authorization': `Bearer ${accessToken}`,
                            'Content-Type': 'application/json',
                        },
                    });
                    const data = await response.json();
                    if (data.error) {
                        alert("Error deleting user: " + data.error);
                        return;
                    }
                    if (!response.ok) {
                        alert("Error deleting user: " + data.message);
                        return;
                    }
                    const responsecheck = await fetch(`/api/v1/users/decode_user`, {
                        method: 'GET',
                        headers: {
                            'Authorization': `Bearer ${accessToken}`,
                            'Content-Type': 'application/json',
                        },
                    });
                    const datacheck = await responsecheck.json();
                    if (datacheck.email === email){
                        console.log(window.location.origin)
                        window.location.href = window.location.origin + '/';
                        return;
                    }
                    else{

                    alert('User deleted successfully!');
                    await fetchAndPopulateProfiles();
                }
                } catch (error) {
                    alert("Error deleting user: " + error.message);
                }
            }
        });

        // Update User Form Submission
        document.getElementById('updateUserForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const email = document.getElementById('update_user_email').value;
            const first_name = document.getElementById('update_first_name').value;
            const last_name = document.getElementById('update_last_name').value;
            const role = document.getElementById('update_role').value;
            const department = document.getElementById('update_department').value || null;
            const phone_number = document.getElementById('update_phone_number').value || null;
            const status = document.getElementById('update_user_status').value;

            // Validate role
            if (!['admin', 'user'].includes(role)) {
                alert("Role must be 'admin' or 'user'.");
                return;
            }

            const formData = {
                first_name,
                last_name,
                email,
                role,
                department,
                phone_number,
                status
            };
            console.log(formData)

            const accessToken = localStorage.getItem('access_token');
            if (!accessToken) {
                alert("No access token found. Please log in.");
                return;
            }

            try {
                const response = await fetch(`/api/v1/users/update_user/${email}`, {
                    method: 'PUT',
                    headers: {
                        'Authorization': `Bearer ${accessToken}`,
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify(formData),
                });
                const data = await response.json();
                if (data.error) {
                    alert("Error updating user: " + data.error);
                    return;
                }
                if (!response.ok) {
                    alert("Error updating user: " + data.message);
                    return;
                }

                alert('User updated successfully!');
                userUpdateModal.style.display = 'none';
                document.body.style.overflow = 'auto';
                await fetchAndPopulateProfiles();
            } catch (error) {
                alert("Error updating user: " + error.message);
            }
        });

        // Close Profile Modal
        profileClose.onclick = function() {
            profileModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        };

        // Close User Update Modal
        userUpdateClose.onclick = function() {
            userUpdateModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        };

        // Close modals when clicking outside
        window.addEventListener('click', function(event) {
            if (event.target == profileModal) {
                profileModal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
            if (event.target == userUpdateModal) {
                userUpdateModal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        });