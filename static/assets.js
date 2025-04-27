const assetsForm = document.getElementById('assetsForm');

assetsForm.addEventListener('submit', async (e) => {
  e.preventDefault(); // Prevent the page from refreshing
  const form = e.target
  const vendor_ids = document.getElementsByClassName('vendor_id');
  //console.log(vendor_ids,Array.from(vendor_ids));
    const vendorIdExists = Array.from(vendor_ids).some(vendor => vendor.innerHTML === form.vendor_id.value);
    if (!vendorIdExists) {
        alert("The vendor ID must be in the list.");
        return;
    }
    
    const formData = {
        medicine_asset: form.medicine_asset.value,
        vendor_id: form.vendor_id.value,
        description: form.description.value,
        category: form.category.value,
        lot_number: form.lot_number.value,
        manufacture_date: form.manufacture_date.value,
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
            alert(asset.error);
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
    updateassetsTable(updatedassets.medicine_assets);
    } else {
        alert("Error creating asset.");
    
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
    <td>${asset.image_url}</td>
`;;
    });
}