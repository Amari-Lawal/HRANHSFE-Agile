const assetsForm = document.getElementById('assetsForm');
        // Modal handling
        
        const assetModal = document.getElementById('assetModal');

        const assetClose = assetModal.querySelector('.close');



        // Open Asset Modal
        document.querySelectorAll('.update-asset').forEach(button => {
            button.addEventListener('click', function() {
                const medicineAsset = this.getAttribute('data-id');
                const row = this.closest('tr');
                const cells = row.getElementsByTagName('td');

                // Populate modal fields
                document.getElementById('update_medicine_id').value = cells[0].innerText;
                document.getElementById('update_medicine_asset').value = cells[1].innerText;
                document.getElementById('update_asset_vendor_id').value = cells[2].innerText;
                document.getElementById('update_description').value = cells[3].innerText;
                document.getElementById('update_category').value = cells[4].innerText;
                document.getElementById('update_lot_number').value = cells[5].innerText;
                document.getElementById('update_manufacture_date').value = cells[6].innerText;
                document.getElementById('update_purchase_cost').value = cells[7].innerText.replace('$', '');
                document.getElementById('update_storage_location').value = cells[8].innerText;
                document.getElementById('update_asset_status').value = cells[9].innerText;
                document.getElementById('update_expiration_date').value = cells[10].innerText;
                document.getElementById('update_storage_conditions').value = cells[11].innerText;
                document.getElementById('update_useful_life_years').value = cells[12].innerText;
                document.getElementById('update_current_stock').value = cells[13].innerText;
                document.getElementById('update_image_url').value = cells[14].querySelector('img') ? cells[14].querySelector('img').src : '';

                assetModal.style.display = 'block';
                document.body.style.overflow = 'hidden';
            });
        });



        // Delete Asset
        document.querySelectorAll('.delete-asset').forEach(button => {
            button.addEventListener('click', async function() {
                const medicineId = this.getAttribute('data-id');
                if (!confirm(`Are you sure you want to delete medicine ID ${medicineId}?`)) {
                    return;
                }

                const accessToken = localStorage.getItem('access_token');
                if (!accessToken) {
                    alert("No access token found. Please log in.");
                    return;
                }

                try {
                    const response = await fetch(`/api/v1/admin/delete_medicine_asset/${medicineId}`, {
                        method: "DELETE",
                        headers: {
                            "Authorization": `Bearer ${accessToken}`,
                            'Content-Type': 'application/json',
                        },
                    });
                    const data = await response.json();
                    if (data.error) {
                        alert("Error deleting asset: " + data.error);
                        return;
                    }
                    if (!response.ok) {
                        alert("Error deleting asset: " + data.message);
                        return;
                    }

                    alert('Asset deleted successfully!');
                    window.location.reload();
                } catch (error) {
                    alert("Error deleting asset: " + error.message);
                }
            });
        });


        assetClose.onclick = function() {
            assetModal.style.display = 'none';
            document.body.style.overflow = 'auto';
        };

        // Close modal when clicking outside
        window.onclick = function(event) {
            if (event.target == assetModal) {
                assetModal.style.display = 'none';
                document.body.style.overflow = 'auto';
            }
        };

       

        // Update Asset Form Submission
        document.getElementById('updateAssetForm').addEventListener('submit', async function(e) {
            e.preventDefault();
            const medicine_id = document.getElementById('update_medicine_id').value;
            const medicine_asset = document.getElementById('update_medicine_asset').value;
            const vendor_id = document.getElementById('update_asset_vendor_id').value;
            const description = document.getElementById('update_description').value;
            const category = document.getElementById('update_category').value;
            const lot_number = document.getElementById('update_lot_number').value;
            const manufacture_date = document.getElementById('update_manufacture_date').value;
            const purchase_cost = document.getElementById('update_purchase_cost').value;
            const storage_location = document.getElementById('update_storage_location').value;
            const status = document.getElementById('update_asset_status').value;
            const expiration_date = document.getElementById('update_expiration_date').value;
            const storage_conditions = document.getElementById('update_storage_conditions').value;
            const useful_life_years = document.getElementById('update_useful_life_years').value;
            const current_stock = document.getElementById('update_current_stock').value;
            const image_url = document.getElementById('update_image_url').value;

            const vendor_ids = document.getElementsByClassName('vendor_id');
            const vendorIdExists = Array.from(vendor_ids).some(vendor => vendor.innerHTML === vendor_id);
            if (!vendorIdExists) {
                alert("The vendor ID must be in the list.");
                return;
            }
            
            //console.log(medicine_asset, vendor_id, description, category, lot_number, manufacture_date, purchase_cost, storage_location, status, expiration_date, storage_conditions, useful_life_years, current_stock, image_url);
            console.log(manufacture_date)
            const formData = {
                medicine_asset:medicine_asset,
                vendor_id:vendor_id,
                description:description,
                category:category,
                lot_number:lot_number,
                manufacture_date:manufacture_date,
                purchase_cost:purchase_cost,
                storage_location:storage_location,
                status:status,
                expiration_date:expiration_date,
                storage_conditions:storage_conditions,
                useful_life_years:useful_life_years,
                current_stock:current_stock,
                image_url:image_url
            };

            const accessToken = localStorage.getItem('access_token');
            if (!accessToken) {
                alert("No access token found. Please log in.");
                return;
            }

            try {
                const response = await fetch(`/api/v1/assets/update_medicine_asset/${medicine_id}`, {
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
                alert('Asset updated successfully!');
                window.location.reload();
            } catch (error) {
                alert("Error updating asset: " + error.message);
            }
        });

document.addEventListener("DOMContentLoaded", function() {
    // Asset update
    const assetButtons = document.querySelectorAll('.update-asset');
    assetButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            const assetId = event.target.dataset.id;
            const assetRow = event.target.closest('tr');
            const medicineAsset = assetRow.querySelector('td:nth-child(1)').textContent;
            const vendorId = assetRow.querySelector('td:nth-child(2)').textContent;
            const description = assetRow.querySelector('td:nth-child(3)').textContent;
            const category = assetRow.querySelector('td:nth-child(4)').textContent;
            const lotNumber = assetRow.querySelector('td:nth-child(5)').textContent;
            const manufactureDate = assetRow.querySelector('td:nth-child(6)').textContent;
            const purchaseCost = assetRow.querySelector('td:nth-child(7)').textContent;
            const status = assetRow.querySelector('td:nth-child(8)').textContent;

            const formData = {
                "medicine_asset": medicineAsset,
                "vendor_id": vendorId,
                "description": description,
                "category": category,
                "lot_number": lotNumber,
                "manufacture_date": manufactureDate,
                "purchase_cost": purchaseCost,
                "status": status
            };
            console.log('Form Data:', formData);
            // Populate the form fields or send an update request
        });
    });
})

assetsForm.addEventListener('submit', async (e) => {
    e.preventDefault(); // Prevent the page from refreshing
    const form = e.target
    const vendor_ids = document.getElementsByClassName('vendor_id');
    //console.log(vendor_ids,Array.from(vendor_ids));
    const vendorIdExists = Array.from(vendor_ids).some(vendor => vendor.innerHTML === form.vendor_id.value);
    if (!vendorIdExists) {
        alert("The vendor ID must be in the list.");
        scrollToVendorsId("vendors-title");
        return;
    }
    console.log(form.manufacture_date.value)
    const formData = {
        medicine_asset: form.medicine_asset.value,
        vendor_id: form.vendor_id.value,
        description: form.description.value,
        category: form.category.value,
        lot_number: form.lot_number.value,
        manufacture_date: form.manufacture_date.value ,
        purchase_cost: form.purchase_cost.value,
        storage_location: form.storage_location.value,
        status: form.status.value,
        expiration_date: form.expiration_date.value,
        storage_conditions: form.storage_conditions.value,
        useful_life_years: form.useful_life_years.value,
        current_stock: form.current_stock.value,
        image_url: form.image_url.value,
    };
    const accessToken = localStorage.getItem('access_token');
    if (!accessToken) {
        alert("No access token found. Please log in.");
        return;
    }
    const response = await fetch("/api/v1/assets/create_medicine_asset", {
        method: "POST",
        headers: {
            "Authorization": `Bearer ${accessToken}`,
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(formData),
    });
    const data = await response.json();
    //console.log(data);

    if (response.ok) {
        // Reload the assets table without refreshing the entire page

        if (data.error) {
            alert(data.error);
            return;
        }
        else if (data.message) {
            alert(data.message);

        }
        const responseasset = await fetch("/api/v1/assets/get_all_medicine_assets", {
            method: "GET",
            headers: {
                "Authorization": `Bearer ${accessToken}`
            },
        });
        const updatedassets = await responseasset.json();
        //console.log(updatedassets);    
        window.location.reload();
        //updateassetsTable(updatedassets.medicine_assets);
        scrollToVendorsId(`assets-table`);
    } else {
        if (data.error){
            alert(data.error)
        }
        else{
            alert("Error creating asset.");
        }
        

    }



    // You can now send assetData in a fetch request if you want
    // Example: fetch('/api/assets', { method: 'POST', body: JSON.stringify(assetData) })

});

function updateassetsTable(assets) {
    const tableBody = document.getElementById('assets-table').getElementsByTagName('tbody')[0];
    tableBody.innerHTML = '';  // Clear existing rows

    assets.forEach(asset => {
        const row = tableBody.insertRow();
        row.innerHTML = `
    <td>${asset.medicine_asset}</td>
    <td>${asset.vendor_id}</td>
    <td>${asset.description}</td>
    <td>${asset.category}</td>
    <td>${asset.lot_number}</td>
    <td>${asset.manufacture_date}</td>
    <td>${asset.purchase_cost}</td>
    <td>${asset.storage_location}</td>
    <td>${asset.status}</td>
    <td>${asset.expiration_date}</td>
    <td>${asset.storage_conditions}</td>
    <td>${asset.useful_life_years}</td>
    <td>${asset.current_stock}</td>
    <td> <img src="${asset.image_url}" alt="Asset Image" /></td>
`;;
    });
}
function scrollToVendorsId(elementId) {
    // Get the vendors table element
    const vendorsTable = document.getElementById(elementId);

    // Scroll to the vendors table
    vendorsTable.scrollIntoView({ behavior: "smooth", block: "start" });
}