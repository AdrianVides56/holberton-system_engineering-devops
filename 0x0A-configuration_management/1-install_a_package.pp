# Using Puppet, install puppet-lint
package {'puppet-lint':
  ensure   => '2.1.2',
  provider => 'gem'
}