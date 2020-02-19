describe command('java -version') do
  its('exit_status') { should eq 0 }
  its('stderr') { should match /Zulu 8/ }
end

describe port('8080') do
  it { should be_listening }
  its('addresses') { should include /127.0.0.1/ }
end

describe port('8443') do
  it { should be_listening }
  its('addresses') { should include /127.0.0.1/ }
end

describe port('80') do
  it { should be_listening }
  its('addresses') { should include /0.0.0.0/ }
end

describe port('443') do
  it { should be_listening }
  its('addresses') { should include /0.0.0.0/ }
end
