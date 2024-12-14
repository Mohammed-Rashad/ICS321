import React, { useState } from 'react';
import { 
  Train, Users, Calendar, Ticket, ListChecks, UserPlus, Shield, UserCog 
} from 'lucide-react';
import { useNavigate } from 'react-router-dom';


// Mock data (in a real app, this would come from an API)
const initialTrains = [
  { 
    name: 'Najran', 
    stations: ['Najran', 'Abha', 'Mecca'], 
    maxPassengers: '34',
    cost: '32',
    id: 1
  }
];

const initialStaff = [
  { 
    id: 1, 
    name: 'John Doe', 
    email: 'john.doe@railway.com',
    role: 'Driver',
    salary: 45000 
  },
  { 
    id: 2, 
    name: 'Alice Smith', 
    email: 'alice.smith@railway.com',
    role: 'Engineer',
    salary: 50000 
  }
];

const initialAdmins = [
  {
    id: 1,
    name: 'Railway Super Admin',
    email: 'admin@railway.com',
    salary: 75000
  }
];

const initialPassengers = [
  { 
    id: 1, 
    name: 'Rahul Kumar', 
    trainName: 'Express Mumbai', 
    status: 'confirmed',
    seat: '12A'
  },
  { 
    id: 2, 
    name: 'Priya Sharma', 
    trainName: 'Express Mumbai', 
    status: 'waitlist',
    seat: null
  }
];

// fetch /train/all to get all trains and put them in the initialTrains array
const fetchTrains = async () => {
  try {
    const response = await fetch('http://localhost:5000/train/all', {
      method: 'GET',
      headers: {
        'Content-Type': 'application/json',
      }
    });
    if (response.ok) {
      const data = await response.json();
      let trainsList = data.Trains;
      console.log('Trains:', trainsList);
      for (let i = 0; i < trainsList.length; i++) {
        const train = {
          name: "Train "  + trainsList[i].trainNumber,
          stations: ["av", "av"],
          maxPassengers: trainsList[i].maxPassengers,
          cost: trainsList[i].cost,
          id: trainsList[i].trainNumber
        };
        initialTrains.push(train);
      }
    }
  } catch (error) {
    console.error('Error fetching trains:', error);
    alert('Failed to fetch trains. Please try again.');
  }
}
fetchTrains();
const RailwayDashboard = () => {
  const [trains, setTrains] = useState(initialTrains);
  const [staff, setStaff] = useState(initialStaff);
  const [admins, setAdmins] = useState(initialAdmins);
  const [passengers, setPassengers] = useState(initialPassengers);
  const [activeSection, setActiveSection] = useState('trains');
  
  // New state for form management
  const [isAddStaffModalOpen, setIsAddStaffModalOpen] = useState(false);
  const [isAddAdminModalOpen, setIsAddAdminModalOpen] = useState(false);
  const [newStaffForm, setNewStaffForm] = useState({
    name: '',
    email: '',
    password: '',
    role: 'Driver',
    salary: ''
  });
  const [newAdminForm, setNewAdminForm] = useState({
    name: '',
    email: '',
    password: '',
    salary: ''
  });
  const [isAddTrainModalOpen, setIsAddTrainModalOpen] = useState(false);
  const [newTrainForm, setNewTrainForm] = useState({
    name: '',
    stations: '',
    maxPassengers: '',
    cost: '',
    id: ''
  });
  // Previous methods remain the same...
  
  // New method to handle staff creation
  const createStaff = (e: any) => {
    e.preventDefault();
    const newStaff = {
      ...newStaffForm,
      id: staff.length + 1,
      salary: parseFloat(newStaffForm.salary)
    };
    setStaff([...staff, newStaff]);
    setIsAddStaffModalOpen(false);
    // Reset form
    setNewStaffForm({
      name: '',
      email: '',
      password: '',
      role: 'Driver',
      salary: ''
    });
  };

  // New method to handle admin creation
  const createAdmin = (e: any) => {
    e.preventDefault();
    const newAdmin = {
      ...newAdminForm,
      id: admins.length + 1,
      salary: parseFloat(newAdminForm.salary)
    };
    setAdmins([...admins, newAdmin]);
    setIsAddAdminModalOpen(false);
    // Reset form
    setNewAdminForm({
      name: '',
      email: '',
      password: '',
      salary: ''
    });
  };

  const createTrain = async (e: React.FormEvent) => {
    e.preventDefault();
    
    try {
      // Prepare train data for backend
      const trainData = {
        name: newTrainForm.name,
        stations: newTrainForm.stations.split(',').map(station => station.trim()),
        max_passengers: parseInt(newTrainForm.maxPassengers),
        cost: parseFloat(newTrainForm.cost),
        id: parseInt(newTrainForm.id)
      };

      // Send POST request to Flask backend
      // const response = await axios.post('http://localhost:5000/api/trains', trainData);
      console.log('Train data:', trainData);
      const response = await fetch('http://localhost:5000/train/insert_train', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
          'Authorization': `Bearer ${localStorage.getItem('token')}`
        },
        body: JSON.stringify(trainData)
      });

      // Only update if backend responds successfully
      if (response.ok) {
        const newTrain = {
          name: trainData.name,
          stations: trainData.stations,
          maxPassengers: trainData.max_passengers.toString(),
          cost: trainData.cost.toString(),
          id: trainData.id
        };

        setTrains([...trains, newTrain]);
        setIsAddTrainModalOpen(false);
        
        // Reset form
        setNewTrainForm({
          name: '',
          stations: '',
          maxPassengers: '',
          cost: '',
          id: ''
        });
      }
    } catch (error) {
      console.error('Error adding train:', error);
      alert('Failed to add train. Please try again.');
    }
  };
  const navigate = useNavigate();
  const signout = async () => {
    // clear local storage
    localStorage.clear();
    await fetch('http://localhost:5000/auth/adminlogout', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      }
    });
    navigate('/adminlogin');
    // redirect to login
    // window.location.href = '/login';
  }
  // New method to render staff management section
  const renderStaffSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <UserCog className="mr-2" /> Staff Management
        </h2>
        <button 
          onClick={() => setIsAddStaffModalOpen(true)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center"
        >
          <UserPlus className="mr-2" /> Add Staff
        </button>
      </div>

      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Name</th>
            <th className="p-3 text-left">Email</th>
            <th className="p-3 text-left">Role</th>
            <th className="p-3 text-left">Salary</th>
          </tr>
        </thead>
        <tbody>
          {staff.map(member => (
            <tr key={member.id} className="border-b">
              <td className="p-3">{member.name}</td>
              <td className="p-3">{member.email}</td>
              <td className="p-3">{member.role}</td>
              <td className="p-3">{member.salary.toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {/* Staff Add Modal */}
      {isAddStaffModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-6 rounded-lg w-96">
            <h3 className="text-xl font-bold mb-4">Add New Staff</h3>
            <form onSubmit={createStaff}>
              <input 
                type="text" 
                placeholder="Name" 
                required
                value={newStaffForm.name}
                onChange={(e) => setNewStaffForm({...newStaffForm, name: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="email" 
                placeholder="Email" 
                required
                value={newStaffForm.email}
                onChange={(e) => setNewStaffForm({...newStaffForm, email: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="password" 
                placeholder="Password" 
                required
                value={newStaffForm.password}
                onChange={(e) => setNewStaffForm({...newStaffForm, password: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <select
                value={newStaffForm.role}
                onChange={(e) => setNewStaffForm({...newStaffForm, role: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              >
                <option value="Driver">Driver</option>
                <option value="Engineer">Engineer</option>
              </select>
              <input 
                type="number" 
                placeholder="Salary" 
                required
                value={newStaffForm.salary}
                onChange={(e) => setNewStaffForm({...newStaffForm, salary: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <div className="flex justify-end space-x-2">
                <button 
                  type="button"
                  onClick={() => setIsAddStaffModalOpen(false)}
                  className="bg-gray-300 text-black px-4 py-2 rounded"
                >
                  Cancel
                </button>
                <button 
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Add Staff
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );

  // New method to render admin management section
  const renderAdminSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <Shield className="mr-2" /> Admin Management
        </h2>
        <button 
          onClick={() => setIsAddAdminModalOpen(true)}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center"
        >
          <UserPlus className="mr-2" /> Add Admin
        </button>
      </div>

      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Name</th>
            <th className="p-3 text-left">Email</th>
            <th className="p-3 text-left">Salary</th>
          </tr>
        </thead>
        <tbody>
          {admins.map(admin => (
            <tr key={admin.id} className="border-b">
              <td className="p-3">{admin.name}</td>
              <td className="p-3">{admin.email}</td>
              <td className="p-3">{admin.salary.toLocaleString()}</td>
            </tr>
          ))}
        </tbody>
      </table>
          
      {/* Admin Add Modal */}
      {isAddAdminModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-6 rounded-lg w-96">
            <h3 className="text-xl font-bold mb-4">Add New Admin</h3>
            <form onSubmit={createAdmin}>
              <input 
                type="text" 
                placeholder="Name" 
                required
                value={newAdminForm.name}
                onChange={(e) => setNewAdminForm({...newAdminForm, name: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="email" 
                placeholder="Email" 
                required
                value={newAdminForm.email}
                onChange={(e) => setNewAdminForm({...newAdminForm, email: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="password" 
                placeholder="Password" 
                required
                value={newAdminForm.password}
                onChange={(e) => setNewAdminForm({...newAdminForm, password: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="number" 
                placeholder="Salary" 
                required
                value={newAdminForm.salary}
                onChange={(e) => setNewAdminForm({...newAdminForm, salary: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <div className="flex justify-end space-x-2">
                <button 
                  type="button"
                  onClick={() => setIsAddAdminModalOpen(false)}
                  className="bg-gray-300 text-black px-4 py-2 rounded"
                >
                  Cancel
                </button>
                <button 
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Add Admin
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
  const renderTrainSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <Train className="mr-2" /> Train Management
        </h2>
        <button 
          onClick={() => {setIsAddTrainModalOpen(true)}}
          className="bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center"
        >
          <Train className="mr-2" /> Add Train
        </button>
      </div>
  
      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Train Name</th>
            <th className="p-3 text-left">Stations</th>
            <th className="p-3 text-left">Max Capacity</th>
            <th className="p-3 text-left">Cost</th>
          </tr>
        </thead>
        <tbody>
          {trains.map(train => (
            <tr key={train.name} className="border-b">
              <td className="p-3">{train.name}</td>
              <td className="p-3">{train.stations.join(', ')}</td>
              <td className='p-3'>{train.maxPassengers}</td>
              <td className='p-3'>S.R {train.cost}</td>
            </tr>
          ))}
        </tbody>
      </table>

      {isAddTrainModalOpen && (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
          <div className="bg-white p-6 rounded-lg w-96">
            <h3 className="text-xl font-bold mb-4">Add New Train</h3>
            <form onSubmit={createTrain}>
              <input 
                type="text" 
                placeholder="Train Name" 
                required
                value={newTrainForm.name}
                onChange={(e) => setNewTrainForm({...newTrainForm, name: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="text" 
                placeholder="Stations (comma-separated)" 
                required
                value={newTrainForm.stations}
                onChange={(e) => setNewTrainForm({...newTrainForm, stations: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="number" 
                placeholder="Max Passengers" 
                required
                value={newTrainForm.maxPassengers}
                onChange={(e) => setNewTrainForm({...newTrainForm, maxPassengers: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="number" 
                placeholder="cost" 
                required
                value={newTrainForm.cost}
                onChange={(e) => setNewTrainForm({...newTrainForm, cost: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <input 
                type="number" 
                placeholder="id" 
                required
                value={newTrainForm.id}
                onChange={(e) => setNewTrainForm({...newTrainForm, id: e.target.value})}
                className="w-full border p-2 mb-2 rounded"
              />
              <div className="flex justify-end space-x-2">
                <button 
                  type="button"
                  onClick={() => setIsAddTrainModalOpen(false)}
                  className="bg-gray-300 text-black px-4 py-2 rounded"
                >
                  Cancel
                </button>
                <button 
                  type="submit"
                  className="bg-blue-500 text-white px-4 py-2 rounded"
                >
                  Add Train
                </button>
              </div>
            </form>
          </div>
        </div>
      )}
    </div>
  );
  
  const renderPassengersSection = () => (
    <div className="p-6">
      <div className="flex justify-between items-center mb-4">
        <h2 className="text-2xl font-bold flex items-center">
          <Users className="mr-2" /> Passengers
        </h2>
      </div>
  
      <table className="w-full bg-white shadow rounded-lg">
        <thead className="bg-gray-100">
          <tr>
            <th className="p-3 text-left">Passenger Name</th>
            <th className="p-3 text-left">Train</th>
            <th className="p-3 text-left">Seat</th>
            <th className="p-3 text-left">Status</th>
          </tr>
        </thead>
        <tbody>
          {passengers.map(passenger => {
            const train = trains.find(train => train.name === passenger.trainName);
            return (
              <tr key={passenger.id} className="border-b">
                <td className="p-3">{passenger.name}</td>
                <td className="p-3">{train ? train.name : 'N/A'}</td>
                <td className="p-3">{passenger.seat || 'N/A'}</td>
                <td className="p-3">{passenger.status}</td>
              </tr>
            );
          })}
        </tbody>
      </table>
      
    </div>
  );
  
  // Update sidebar and content rendering
  return (
    <div className="min-h-screen bg-gray-100 flex">
      {/* Sidebar */}
      <div className="w-64 bg-white shadow-md">
        <div className="p-4 text-2xl font-bold border-b">
          Railway Admin
          <button onClick={signout} className={"bg-blue-500 text-white px-4 py-2 rounded hover:bg-blue-600 flex items-center text-xs"}>Sign Out</button>
        </div>
        
        {/* // add signout button here.  */}
        
        <nav className="p-4">
          <button 
            onClick={() => setActiveSection('trains')}
            className={`flex items-center w-full p-2 rounded mb-2 ${
              activeSection === 'trains' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <Train className="mr-2" /> Trains
          </button>
          <button 
            onClick={() => setActiveSection('passengers')}
            className={`flex items-center w-full p-2 rounded mb-2 ${
              activeSection === 'passengers' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <Users className="mr-2" /> Passengers
          </button>
          <button 
            onClick={() => setActiveSection('staff')}
            className={`flex items-center w-full p-2 rounded mb-2 ${
              activeSection === 'staff' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <UserCog className="mr-2" /> Staff
          </button>
          <button 
            onClick={() => setActiveSection('admins')}
            className={`flex items-center w-full p-2 rounded ${
              activeSection === 'admins' 
                ? 'bg-blue-500 text-white' 
                : 'hover:bg-gray-200'
            }`}
          >
            <Shield className="mr-2" /> Admins
          </button>
        </nav>
      </div>

      {/* Main Content */}
      <div className="flex-1">
        {activeSection === 'trains' && renderTrainSection()}
        {activeSection === 'passengers' && renderPassengersSection()}
        {activeSection === 'staff' && renderStaffSection()}
        {activeSection === 'admins' && renderAdminSection()}
      </div>
    </div>
  );
};

export default RailwayDashboard;