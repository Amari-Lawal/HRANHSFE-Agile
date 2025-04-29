const vendorForm = document.getElementById('vendorForm');
// Open Vendor Modal
const vendorModal = document.getElementById('vendorModal');
const vendorClose = vendorModal.querySelector('.close');
document.querySelectorAll('.update-vendor').forEach(button => {
    button.addEventListener('click', function() {
        const vendorId = this.getAttribute('data-id');
        const row = this.closest('tr');
        const cells = row.getElementsByTagName('td');

        // Populate modal fields
        document.getElementById('update_vendor_id').value = vendorId;
        document.getElementById('update_vendor_name').value = cells[1].innerText;
        document.getElementById('update_vendor_address').value = cells[2].innerText;
        document.getElementById('update_contact_person').value = cells[3].innerText;
        document.getElementById('update_contact_number').value = cells[4].innerText;
        document.getElementById('update_email').value = cells[5].innerText;
        document.getElementById('update_status').value = cells[6].innerText;

        vendorModal.style.display = 'block';
        document.body.style.overflow = 'hidden';
    });
});
document.addEventListener("DOMContentLoaded", function() {
                // Vendor update
                const vendorButtons = document.querySelectorAll('.update-vendor');
                vendorButtons.forEach(button => {
                    button.addEventListener('click', function(event) {
                        const vendorId = event.target.dataset.id;
                        const vendorRow = event.target.closest('tr');
                        const vendorName = vendorRow.querySelector('td:nth-child(2)').textContent;
                        const vendorAddress = vendorRow.querySelector('td:nth-child(3)').textContent;
                        const contactPerson = vendorRow.querySelector('td:nth-child(4)').textContent;
                        const contactNumber = vendorRow.querySelector('td:nth-child(5)').textContent;
                        const email = vendorRow.querySelector('td:nth-child(6)').textContent;
                        const status = vendorRow.querySelector('td:nth-child(7)').textContent;
    
                        const formData = {
                            "vendor_name": vendorName,
                            "vendor_address": vendorAddress,
                            "contact_person": contactPerson,
                            "contact_number": contactNumber,
                            "email": email,
                            "status": status
                        };
                        console.log('Form Data:', formData);
                        // Populate the form fields or send an update request
                    });
                });
})

     
vendorForm.addEventListener('submit', async (e) => {
  e.preventDefault(); // Prevent the page from refreshing
  const form = e.target
    const formData = {
        vendor_name: form.vendor_name.value,
        vendor_address: form.vendor_address.value,
        contact_person: form.contact_person.value,
        contact_number: form.contact_number.value,
        email: form.email.value,
        status: form.status.value
    };
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
        alert("No access token found. Please log in.");
        return;
    }
    const response = await fetch("/api/v1/vendors/create_vendor", {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });
    const data = await response.json();
    console.log(data);

    if (response.ok) {
        // Reload the vendors table without refreshing the entire page
        
        if (data.error) {
            alert(data.error);
            return;
        }
        else if (data.message) {
            alert(data.message);
        }
        const responsevendor = await fetch("/api/v1/vendors/get_all_vendors", {
        method: "GET",
        headers: {
            "Authorization": `Bearer ${accessToken}`
        },
    });
    const updatedVendors = await responsevendor.json();
    console.log(updatedVendors);    
    window.location.reload();
    //updateVendorsTable(updatedVendors.vendors);
    scrollToVendorsId("vendors-title");
    } else {
        alert("Error creating vendor.");
    
    } 
        

  
  // You can now send vendorData in a fetch request if you want
  // Example: fetch('/api/vendors', { method: 'POST', body: JSON.stringify(vendorData) })

});

// Delete Vendor
document.querySelectorAll('.delete-vendor').forEach(button => {
    button.addEventListener('click', async function() {
        const vendorId = this.getAttribute('data-id');
        if (!confirm(`Are you sure you want to delete vendor ID ${vendorId}?`)) {
            return;
        }

        const accessToken = localStorage.getItem('access_token');
        if (!accessToken) {
            alert("No access token found. Please log in.");
            return;
        }

        try {
            const response = await fetch(`/api/v1/admin/delete_vendor/${vendorId}`, {
                method: "DELETE",
                headers: {
                    "Authorization": `Bearer ${accessToken}`,
                    'Content-Type': 'application/json',
                },
            });
            const data = await response.json();
            if (data.error) {
                alert("Error deleting vendor: " + data.error);
                return;
            }
            if (!response.ok) {
                alert("Error deleting vendor: " + data.message);
                return;
            }

            alert('Vendor deleted successfully!');
            window.location.reload();
        } catch (error) {
            alert("Error deleting vendor: " + error.message);
        }
    });
});
 // Update Vendor Form Submission
 document.getElementById('updateVendorForm').addEventListener('submit', async function(e) {
    e.preventDefault();
    const vendorId = document.getElementById('update_vendor_id').value;
    const vendor_name = document.getElementById('update_vendor_name').value;
    const vendor_address = document.getElementById('update_vendor_address').value;
    const contact_person = document.getElementById('update_contact_person').value;
    const contact_number = document.getElementById('update_contact_number').value;
    const email = document.getElementById('update_email').value;
    const status = document.getElementById('update_status').value;
    console.log(vendorId, vendor_name, vendor_address, contact_person, contact_number, email, status);
    const formData = {
        vendor_name,
        vendor_address,
        contact_person,
        contact_number,
        email,
        status
    };
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
        alert("No access token found. Please log in.");
        return;
    }

    try {
        const response = await fetch(`/api/v1/vendors/update_vendor/${vendorId}`, {
            method: "PUT",
            headers: {
                "Authorization": `Bearer ${accessToken}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData),
        });
        const data = await response.json();
        console.log(data);
        if (data.error) {
            alert("Error updating asset: " + data.error);
            return;
        }
        if (!response.ok) {
            alert("Error updating asset: " + data.message);
            return;
        }

        assetModal.style.display = 'none';
        document.body.style.overflow = 'auto';
        alert('Vendor updated successfully!');
        window.location.reload();
    } catch (error) {
        alert("Error updating asset: " + error.message);
    }
    

    // Optionally, send data to server here
});

// Close modal
vendorClose.onclick = function() {
    vendorModal.style.display = 'none';
    document.body.style.overflow = 'auto';
};
window.onclick = function(event) {
    if (event.target == vendorModal) {
        vendorModal.style.display = 'none';
        document.body.style.overflow = 'auto';
    }
}

// Custom :contains selector for case-sensitive text matching
document.querySelectorAll('td.vendor_id').forEach(td => {
    td.contains = function(text) {
        return this.innerText === text;
    };
});

function updateVendorsTable(vendors) {
    const tableBody = document.getElementById('vendors-table').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';  // Clear existing rows

    vendors.forEach(vendor => {
        const row = tableBody.insertRow();
        row.innerHTML = `
            <td>${vendor.vendor_id}</td>
            <td>${vendor.vendor_name}</td>
            <td>${vendor.vendor_address}</td>
            <td>${vendor.contact_person}</td>
            <td>${vendor.contact_number}</td>
            <td>${vendor.email}</td>
            <td>${vendor.status}</td>
            <td>${vendor.created_at}</td>
            <td>${vendor.updated_at}</td>
        `;
    });
}
function scrollToVendorsId(elementId) {
    // Get the vendors table element
    const vendorsTable = document.getElementById(elementId);

    // Scroll to the vendors table
    vendorsTable.scrollIntoView({ behavior: "smooth", block: "start" });
}